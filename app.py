from flask import Flask, request, jsonify, render_template
from src.helper import download_embedding
from langchain.vectorstores import Pinecone
from pinecone import ServerlessSpec
from pinecone import Pinecone as PCClient
from langchain_pinecone import PineconeVectorStore

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os
from src.helper import get_text_chunk
from werkzeug.utils import secure_filename
from src.helper import load_doc


app = Flask(__name__)

load_dotenv()
pc_key = os.getenv("PINECONE_API_KEY")
pc_env = os.getenv("PINECONE_API_ENV")

embeddings = download_embedding()
pc_client = PCClient(api_key=pc_key, environment=pc_env)


my_index=os.getenv("INDEX_NAME")


prompt = PromptTemplate(template = prompt_template,inpit_variables=['context','question'])
chain_type_kwargs = {"prompt":prompt}


llm = CTransformers(model="C:\\Users\\LOQ\\.cache\\huggingface\\hub\\models--TheBloke--Llama-2-7B-Chat-GGML\\snapshots\\76cd63c351ae389e1d4b91cab2cf470aab11864b\\llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={"max_new_tokens": 512, "temperature": 0.8}
                    )



@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    msg = request.form.get('msg')
    file = request.files.get('file')
    input = msg

    if file:
        file_path = os.path.join('data',secure_filename(file.filename))
        file.save(file_path)
        extracted_data = load_doc(file_path)
        text_chunk = get_text_chunk(extracted_data)
        doc_search = PineconeVectorStore.from_texts(
            [t.page_content for t in text_chunk],
            embedding = embeddings,
            index_name = my_index
            )
        qa = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = "stuff",
            retriever = doc_search.as_retriever(search_kwargs={"k":2}),
            return_source_documents = True,
            chain_type_kwargs = chain_type_kwargs
            )
        result = qa({"query": input})
        print("Response:", result["result"])
        return str(result["result"])

    return f"Sorry, I can only process files. Please upload a PDF file."

if __name__ == '__main__':
    app.run(debug=True)
from src.helper import load_doc, get_text_chunk, download_huggingface_embedding
from langchain.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
import pinecone
from dotenv import load_dotenv
from pinecone import Pinecone,ServerlessSpec



import os
load_dotenv()
pc_key = os.getenv("PINECONE_API_KEY")
pc_env = os.getenv("PINECONE_API_ENV")





text_chunk = get_text_chunk(extracted_data)
embedding = download_huggingface_embedding()

pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )
my_index = 'neww'
    # Now do stuff
if 'neww' not in pc.list_indexes().names():
    pc.create_index(
            name='neww',
            dimension=384,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
#Creating embedding for each textchunks
doc_search = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunk],
    embedding=embedding,
    index_name=my_index
)

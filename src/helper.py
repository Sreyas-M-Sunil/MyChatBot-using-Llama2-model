from langchain.document_loaders import  PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

#Loading data 
def load_doc(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

#Splitting the documents
def split_doc(extracted_data):
    split = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=20)
    text_chunks = split.split_documents(extracted_data)
    return text_chunks

#Accessing the text_chunks
def get_text_chunk(extracted_data):
    text_chunk = split_doc(extracted_data)
    return text_chunk

#Download the embedding model
def download_embedding():
    embeddings = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


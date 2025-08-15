from flask import Flask, request , jasonify, render_template
from src.helper import download_embedding
from langchain.vectorstores import Pinecone
from pinecone import ServerlessSpec
from pinecone import Pinecone as PCClient
from langchain_pinecone import PineconeVectorStore

from langchain.prompts import PromtTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os
from src.helper import get_text_chunk


app = Flask(__name__)

load_dotenv()
pc_key = os.getenv("PINECONE_API_KEY")
pc_env = os.getenv("PINECONE_API_ENV")



from src.helper import load_pdf, text_split

extracted_data = load_pdf("path/to/uploaded.pdf")
chunks = text_split(extracted_data)

# 📚 MyChatBot using LLaMA 2 + LangChain + Pinecone

An intelligent chatbot that can read and answer questions from PDF files using **LLaMA 2**, **LangChain**, and **Pinecone**.  
Users can upload a PDF, and the bot will extract, chunk, and index the content for efficient question answering.

---

## 🚀 Features
- Upload PDF files and query their content
- Uses **LLaMA 2** (via Hugging Face) as the LLM
- **LangChain** for document processing & retrieval
- **Pinecone** for vector database and semantic search
- Simple **Flask** web app backend
- Supports conversational Q&A with source documents

---

## Project Structure
MyChatBot-using-Llama2-model/
│── app.py # Flask app (main entry)
│── helper.py # Helper functions (load PDF, chunk text, etc.)
│── store_index.py # Pinecone index handling
│── chat.html # Frontend chat UI
│── style.css # Styling for frontend
│── requirements.txt # Python dependencies
│── .env # Environment variables (ignored in git)
│── .gitignore # Ignore sensitive/unnecessary files
│── uploads/ # Folder to store uploaded PDFs

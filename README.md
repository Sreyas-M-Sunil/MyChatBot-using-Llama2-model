# 🤖 MyChatBot using LLaMA 2 + LangChain + Pinecone  

A chatbot application that allows users to upload PDF documents and interact with them using natural language. The chatbot is powered by **LLaMA 2**, **LangChain**, and **Pinecone** for semantic search and retrieval.  

---

## ✨ Features
- 📂 Upload PDF files and process them.  
- 🔎 Chunk text and create embeddings.  
- 🌲 Store embeddings in **Pinecone** vector database.  
- 💬 Ask questions and retrieve context-aware answers.  
- 🌐 Simple **Flask-based frontend** with chat interface.  

---

## 📂 Project Structure  

```plaintext
MyChatBot-using-Llama2-model/
│── app.py              # Flask app (main entry)
│── helper.py           # Helper functions (load PDF, chunk text, etc.)
│── store_index.py      # Pinecone index handling
│── chat.html           # Frontend chat UI
│── style.css           # Styling for frontend
│── requirements.txt    # Python dependencies
│── .env                # Environment variables (ignored in git)
│── .gitignore          # Ignore sensitive/unnecessary files
│── uploads/            # Folder to store uploaded PDFs

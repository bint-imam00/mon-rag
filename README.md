# 🤖 RAG Chatbot — Retrieval-Augmented Generation System

> **Built with Python · LlamaIndex · Svelte · JavaScript**  
> An intelligent Q&A system that answers questions based on your own documents — powered by RAG architecture.

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a cutting-edge AI technique that combines:
- 🔍 **Retrieval** — searching relevant information from a knowledge base
- 🧠 **Generation** — producing accurate, context-aware answers using an LLM

Unlike standard chatbots, a RAG system **only answers from your data** — no hallucinations, no off-topic responses.

---

## ✨ Features

- **📄 Document Ingestion** — Load and index custom documents (PDF, TXT, etc.)
- **🔍 Semantic Search** — Find the most relevant passages using vector embeddings
- **💬 Conversational Q&A** — Ask natural language questions, get grounded answers
- **💾 Persistent Storage** — Indexed data saved locally for fast reloading
- **🌐 Web Interface** — Clean frontend built with Svelte for easy interaction

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI / RAG Engine | LlamaIndex (Python) |
| LLM Integration | OpenAI / Local LLM |
| Vector Storage | Local index (persistent) |
| Backend | Python |
| Frontend | Svelte + JavaScript |
| Data | Custom documents (data/ folder) |

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/bint-imam00/mon-rag.git
cd mon-rag
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your documents
Place your files (PDF, TXT, DOCX) in the `data/` folder.

### 5. Run the app
```bash
python main.py
```

---

## 📂 Project Structure

```
mon-rag/
│
├── data/           # Your knowledge base documents
├── storage/        # Persistent vector index storage
├── main.py         # RAG engine & backend logic
├── requirements.txt
└── README.md
```

---

## 💡 Use Cases

This system can be adapted for:
- 📚 **Document Q&A** — Ask questions on legal, medical, or technical documents
- 🏢 **Internal Knowledge Base** — Company policy or HR chatbot
- 🎓 **Education** — Students querying course materials
- 🌍 **African Languages Support** — Adaptable for Wolof, French, Arabic contexts

---

## 🔧 Customization

- Swap the LLM (OpenAI → Mistral, LLaMA, Gemini)
- Change embedding model for multilingual support
- Extend frontend for specific business use cases

---

## 👩🏾‍💻 Author

**Aïcha Mbaye** — AI & Data Science Developer  
CTO @ Art'beau-rescence | Big Data Graduate, Dakar Institute of Technology  
📍 Dakar, Senegal

> Available for freelance missions in AI development, RAG systems, and LLM integration.  
> 🔗 [GitHub Profile](https://github.com/bint-imam00)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

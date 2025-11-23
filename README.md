# **🤖 Multi-Provider CLI Chatbot**

A modular, terminal-based AI chatbot that supports **Ollama**, **LM Studio**, and **LocalAI (Mudler)** — all using **OpenAI-compatible APIs**.
Built with a clean, scalable architecture using **Python**, **Rich**, and **OpenAI SDK**.

---

## 📌 **Project Description**

This project provides a **streaming markdown-based CLI chatbot** that can dynamically switch between different AI providers.
It uses a fully modular structure (providers, UI, chat engine) for maintainability and future expansion.

---

## 🧰 **Tech Stack**

| Component              | Technology                          |
| ---------------------- | ----------------------------------- |
| **Language**           | Python 3.9+                         |
| **CLI UI Rendering**   | `rich`                              |
| **AI Client**          | `openai` (OpenAI-compatible mode)   |
| **Local AI Providers** | Ollama / LM Studio / LocalAI        |
| **Architecture**       | Modular Python package (app folder) |

---

## 🗂️ **Project Structure**

```
project/
│
├── app.py
│
└── app/
    ├── providers.py
    ├── ui.py
    ├── chat.py
    └── __init__.py
```

---

## 🚀 **Features**

* 🔌 Choose between **Ollama**, **LM Studio**, or **LocalAI**
* ⚙️ Fully modular design for easy extension
* 📜 Real-time streaming output rendered via `rich`
* 🧩 OpenAI-compatible API usage
* 🖥️ Clean terminal UI with markdown rendering
* 🔄 Conversation history preserved per session

---

# 🛠️ **Setup Instructions**

Follow these steps to install and run the chatbot.

---

## 1️⃣ **Install Python Requirements**

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## 2️⃣ **Install & Run Any Provider**

You can choose any provider. Each runs locally.

---

### **🔷 A) LM Studio**

Download & install:
[https://lmstudio.ai/](https://lmstudio.ai/)

Run the server:

1. Open LM Studio
2. Go → "Developer" tab
3. Start Local Server (default: [http://localhost:1234/v1](http://localhost:1234/v1))

---

### **🔶 B) Ollama**

Install:
[https://ollama.com/download](https://ollama.com/download)

List models:

```bash
ollama list
```

Start server automatically runs with Ollama.

---

### **🟩 C) LocalAI (Mudler)**

GitHub:
[https://github.com/mudler/LocalAI](https://github.com/mudler/LocalAI)

Docker example:

```bash
docker run -p 8080:8080 localai/localai:latest
```

This exposes the OpenAI-compatible API at:

```
http://localhost:8080/v1
```

---

## 3️⃣ **Project Configuration**

Providers are defined inside:

```
app/providers.py
```

You can modify base URLs or API keys here.

Example:

```python
PROVIDERS = {
    "Ollama": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama-key"
    },
    "LMStudio": {
        "base_url": "http://localhost:1234/v1",
        "api_key": "lm-studio"
    },
    "LocalAI (Mudler)": {
        "base_url": "http://localhost:8080/v1",
        "api_key": "localai-key"
    }
}
```

---

## 4️⃣ **Run the Chatbot**

From project root:

```bash
python app.py
```

---

# 📄 **License**

**`License: MIT — see LICENSE`**

---

# LLaMA Chatbot

A simple RESTful chatbot service powered by a local LLaMA model and served via FastAPI. Sends AI-generated responses to user messages through a `/chat` endpoint.

---

## Postman Demo
> Here's a sample interaction with the chatbot using Postman:
![image](https://github.com/user-attachments/assets/78e7d86f-ebe2-42ec-8960-8b26755e5729)

---
## Overview

- REST API using FastAPI
- Language model: LLaMA (local `.gguf`)
- Receives messages, returns AI-generated text

---

## Project Structure

```graphql
llama_chatbot/
├── app/             
│   ├── main.py         # FastAPI app with /chat endpoint
│   └── model.py        # LLaMA model logic and text generation
└── models/             # Folder to place your .gguf model file
├── requirements.txt    # Python packages
├── README.md           # Project documentation

```

---

## Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/maha-n-tesh/llama_chatbot.git
cd llama_chatbot
```

### Step 2: Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Model Setup

### Download the Model (.gguf format)

You can download the required model manually from Hugging Face:

[Click here to download `llama-2-7b-chat.Q4_K_M.gguf`](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf)

- LLaMA models are large and not included in this repo.
- Place the file inside the `models/` directory.

---

## Running the API

```bash
uvicorn app.main:app --reload
```

Access the API at:

```
http://127.0.0.1:8000
```

---

## How to Test the Chatbot

### Swagger UI

Visit:

```
http://127.0.0.1:8000/docs
```

Try the `/chat` endpoint with:

```json
{
  "message": "Hello, who created you?"
}
```

---

### Postman Example

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/chat`
- **Body:** JSON

```json
{
  "message": "write a code to check the number is even or odd"
}
```

---

## Prompt Format Used

This chatbot uses LLaMA's `[INST] ... [/INST]` format for clearer and more structured AI responses:

```python
formatted_prompt = f"[INST] {user_input} [/INST]"
```

It also uses stop tokens like `["</s>", "User:", "Assistant:"]` to avoid long or hallucinated replies.

---

## Tech Stack

- Python 3.11+
- FastAPI
- llama-cpp-python
- Uvicorn
- LLaMA model (`.gguf` format)

---

## Known Limitations

- LLaMA is an offline model — it can hallucinate or guess facts
- Responses are best-effort and may not reflect real-time knowledge
- No frontend included (API only)

from fastapi import FastAPI
from pydantic import BaseModel
from app.model import llama_response

app = FastAPI()

class ChatRequest(BaseModel):
    message : str

class ChatResponse(BaseModel):
    response : str
    
@app.post('/chat', response_model = ChatResponse)
def chat(request : ChatRequest):
    response_txt = llama_response(request.message)
    return {"response" : response_txt}

@app.get('/')
def root():
    return {"Message" : "Welcome to the LLaMA Chatbot API. Use /chat with POST."}

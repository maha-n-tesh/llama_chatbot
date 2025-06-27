from llama_cpp import Llama
import os

model_path = os.path.join("models","llama-2-7b-chat.Q4_K_M.gguf")
llm = Llama(model_path = model_path, n_ctx = 2048)

def llama_response(prompt : str):
    if not prompt or prompt.strip() == "":
        return {"response" : "Please enter a valid question."}
    
    formatted_prompt = f"[INST] {prompt} [/INST]"
    output = llm(formatted_prompt, max_tokens = 100, stop = ["</s>", "User:", "Assistant:"])
    return output["choices"][0]["text"].strip()
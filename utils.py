# utils.py
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b"   # or gemma:7b if you prefer

def run_local_llm(system_prompt: str, user_text: str) -> str:
    """
    Call Ollama local LLM and return text output.
    """
    prompt = f"{system_prompt}\n\n{user_text}"

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=300)
    response.raise_for_status()

    data = response.json()
    return data["response"].strip()

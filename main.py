import requests
import json
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Prompt(BaseModel):
    prompt_text: str

    def __init__(self, prompt_text = ""):
        self.prompt_text = prompt_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ollama")
def ollama_request(prompt):
    # p = Prompt()
    # p.prompt_text = prompt
    
    url = "http://localhost:11434/api/chat"

    def llama3(prompt):
        data = {
            "model": "llama3.1",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()["message"]["content"]

    response = llama3(prompt)
    print(response)

    # p.response = response
    response = {
        'prompt': prompt,
        'result': response
    }
    return response

@app.get("/ollama/{prompt}")
def ollama_query(prompt: str):
    url = "http://localhost:11434/api/chat"

    def llama3(prompt):
        data = {
            "model": "llama3.1",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()["message"]["content"]

    response = llama3(prompt)
    print(response)
    return {"response": response }
import requests
import json
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

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
from os import getenv
import openai
import requests
import json

openai.organization = "org-wVPDySoWpfji41ZecNs6aEyZ"
openai.api_key = getenv("OPENAPI_TOKEN")
# openai.Model.list()

headers = {
        "Content-Type":"application/json",
        "Authorization":"Bearer "
    }


def mic_check(headers):
    url = "https://api.openai.com/v1/chat/completions"
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello, World!"}],
        "temperature": 0
    }
    request = requests.post(url,headers=headers,json=payload)
    return request.content

def list_models(headers):
    url = "https://api.openai.com/v1/models"

    request = requests.get(url, headers=headers)
    return request.json()

def create_image(headers):
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "prompt": "a cow giving birth to a moose",
        "n":2,
        "size": "512x512"
    }
    request = requests.post(url,headers=headers,json=payload)
    return request.content


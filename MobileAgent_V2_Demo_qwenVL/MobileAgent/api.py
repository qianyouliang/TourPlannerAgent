import base64
import requests
from openai import OpenAI
from dashscope import MultiModalConversation

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def inference_chat(chat, model, api_url, token):
    # Add headers to the request
    headers = {
        "Content-Type": "text/html",
        "Retry-After": "3600",
        "Authorization": f"Bearer {token}"
    }
    
    # Make the request using the headers
    client = OpenAI(api_key=token, base_url=api_url) 
    completion = client.chat.completions.create(
        max_tokens=2048,
        model=model,
        messages=chat,
        temperature=0.0,
        seed=1234,
        headers=headers  # Add custom headers here
    )
    
    print(completion)
    return completion.choices[0].message.content

def call_with_local_file(chat, api_key, model):
    # Add headers to the request
    headers = {
        "Content-Type": "text/html",
        "Retry-After": "3600",
        "Authorization": f"Bearer {api_key}"
    }

    # Make the request using headers
    response = MultiModalConversation.call(model=model, messages=chat, api_key=api_key, headers=headers)
    return response.output.choices[0].message.content[0]["text"]

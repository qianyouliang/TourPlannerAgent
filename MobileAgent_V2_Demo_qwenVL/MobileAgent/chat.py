import copy
from MobileAgent.api import encode_image
from openai import OpenAI

def init_action_chat():
    operation_history = []
    sysetm_prompt = "You are a helpful AI mobile phone operating assistant. You need to help me operate the phone to complete the user\'s instruction."
    operation_history.append(["system", [{"type": "text", "text": sysetm_prompt}]])
    return operation_history


def init_reflect_chat():
    operation_history = []
    sysetm_prompt = "You are a helpful AI mobile phone operating assistant."
    operation_history.append(["system", [{"type": "text", "text": sysetm_prompt}]])
    return operation_history


def init_memory_chat():
    operation_history = []
    sysetm_prompt = "You are a helpful AI mobile phone operating assistant."
    operation_history.append(["system", [{"type": "text", "text": sysetm_prompt}]])
    return operation_history

def inference_chat_v2(chat, model, api_url, api_key):
    messages = []
    client = OpenAI(api_key=api_key, base_url=api_url)
    for role, content in chat:
        messages.append({"role": role, "content": content})
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content
a_rl = "https://dashscope.aliyuncs.com/compatible-mode/v1"
#i_ey = "sk-f7aa51ea4e4642689a8b1b9aad83b04e"
# print(inference_chat_v2(chat=, api_url=api_url, model="qwen-vl-plus", api_key=api_key))
def add_response(role, prompt, chat_history, image=None):
    new_chat_history = copy.deepcopy(chat_history)
    if image:
        content = [
            {
                'text': prompt
            },
            {
                'image': image
            },
        ]
    else:
        content = [
            {
            "text": prompt
            },
        ]
    new_chat_history.append({'role': role, 'content': content})
    return new_chat_history


def add_response_two_image(role, prompt, chat_history, image):
    new_chat_history = copy.deepcopy(chat_history)
    content = [
        {
            "text": prompt
        },
        {
            'image': image[0]
        },
        {
            'image': image[1]
        },
    ]

    new_chat_history.append([role, content])
    return new_chat_history


def print_status(chat_history):
    print("*"*100)
    for chat in chat_history:
        print("role:", chat[0])
        print(chat[1][0]["text"] + "<image>"*(len(chat[1])-1) + "\n")
    print("*"*100)
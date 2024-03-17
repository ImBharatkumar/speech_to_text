import requests
from datasets import load_dataset


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("D:\\Projects\speech_to_text\\src\data\\Recording.m4a")
print(output)



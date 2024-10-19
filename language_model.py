import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Please check the .env file and make sure it's loaded correctly.")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message['content']) 
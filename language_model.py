import os
import dotenv
from openai import OpenAI
from dotenv import load_dotenv

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key = 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)  # Pass the API key here

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
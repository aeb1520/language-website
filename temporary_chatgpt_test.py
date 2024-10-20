
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

# print(os.getenv('OPENAI_API_KEY')) 




MODEL="gpt-4o"

# note that this didn't originally come with the function, that's just so I can test importing a function for front end and back end integration in the flask-app
def very_basic_test_function():
  completion = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "system", "content": "You are a helpful assistant that helps me with my math homework!"},
      {"role": "user", "content": "Hello! Could you solve 20 x 5?"}
    ]
  )
  print("Assistant: " + completion.choices[0].message.content) 



# I'm actually testing with this one so that the text input is incorporated
def echo_word(text):
    prompt = (
        f"Repeat this word back to me: {text}"
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    echoed_response = response.choices[0].message.content
    return echoed_response

def fancy_print(text):
   return ("This is the fancy print of the received text: " + text)



# extra comment so I can commit the changes
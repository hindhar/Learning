import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('/Users/robhindhaugh/Documents/GitHub/Learning/key.env')

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("API key not found. Please ensure it is correctly set in the key.env file.")

client = OpenAI(api_key=openai_api_key)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access to it
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=1
    )
    return response.choices[0].message.content.strip()

user_input = input("Enter your prompt: ")

response = generate_response(user_input)

print(response)

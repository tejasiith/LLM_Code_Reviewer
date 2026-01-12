from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI()

code = """
def add(a, b):
    return a + b
"""

prompt = f"""
Explain what the following Python code does:

{code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

code = """
def multiply(a, b):
    return a * b
"""

prompt = f"""
Generate a professional Python docstring
for each function in the following code.

Code:
{code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)

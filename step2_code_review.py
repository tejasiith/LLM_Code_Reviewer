from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

code = """
def divide(a, b):
    return a / b
"""

prompt = f"""
You are a senior Python developer.

Analyze the following code and provide:
1. What the code does
2. Possible bugs or issues
3. Suggestions for improvement

Code:
{code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

print(response.choices[0].message.content)
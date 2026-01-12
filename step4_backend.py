from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

def review_code(code):
    prompt = f"""
You are an expert Python code reviewer.

Return:
1. Code explanation
2. Bugs or issues
3. Improvements
4. Function-level docstrings

Code:
{code}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


# Test
sample_code = """
def square(x):
    return x*x
"""

print(review_code(sample_code))

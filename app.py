import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

def review_code(code):
    if not code.strip():
        return "Please paste some Python code."

    prompt = f"""
You are an expert Python code reviewer.

Analyze the following Python code and provide:
1. Explanation
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


with gr.Blocks() as demo:
    gr.Markdown("# 🧠 LLM-Based Code Reviewer & Bug Finder")

    code_input = gr.Code(label="Paste Python Code", language="python")
    output = gr.Markdown()

    button = gr.Button("Analyze Code")
    button.click(review_code, code_input, output)

demo.launch()

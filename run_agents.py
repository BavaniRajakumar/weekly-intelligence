import os
from prompts import AGENT_PROMPT

from openai import OpenAI
import anthropic
import google.generativeai as genai


def gpt_agent():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "system", "content": AGENT_PROMPT}]
    )
    return "=== GPT ===\n" + response.choices[0].message.content


def claude_agent():
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        messages=[{"role": "user", "content": AGENT_PROMPT}]
    )
    return "=== CLAUDE ===\n" + response.content[0].text


def gemini_agent():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(AGENT_PROMPT)
    return "=== GEMINI ===\n" + response.text


if __name__ == "__main__":
    print("Running research agents...")

    outputs = []

    if os.getenv("OPENAI_API_KEY"):
        outputs.append(gpt_agent())

    if os.getenv("ANTHROPIC_API_KEY"):
        outputs.append(claude_agent())

    if os.getenv("GEMINI_API_KEY"):
        outputs.append(gemini_agent())

    with open("research_outputs.txt", "w") as f:
        f.write("\n\n".join(outputs))

    print("Research complete. Output saved to research_outputs.txt")

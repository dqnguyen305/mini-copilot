import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "katanemo/Arch-Router-1.5B:hf-inference")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN is not set in .env")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)


def call_ai(messages, max_tokens: int = 512) -> dict:
    """
    Gọi Chat Completion trên HuggingFace Router.
    messages: list[{"role": "...", "content": "..."}]
    """
    try:
        completion = client.chat.completions.create(
            model=HF_MODEL,
            messages=messages,
            max_tokens=max_tokens,
        )
        msg = completion.choices[0].message
        # openai v1: message.content là string
        return {"output": msg.content}
    except Exception as e:
        return {"error": str(e)}

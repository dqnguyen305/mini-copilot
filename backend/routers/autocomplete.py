from fastapi import APIRouter
from models.schemas import CodeInput
from utils.ai_client import call_ai

router = APIRouter(prefix="/autocomplete", tags=["autocomplete"])

@router.post("/")
def autocomplete(payload: CodeInput):
    lang = payload.language or "code"

    system_prompt = (
        "You are an AI coding assistant. Only continue the given code. "
        "Do not repeat existing code. Do not explain."
    )

    user_prompt = (
        f"Continue this {lang} code:\n\n"
        f"{payload.code}\n\n"
        "Only generate the continuation."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return call_ai(messages, max_tokens=150)

from fastapi import APIRouter
from models.schemas import SummarizeInput
from utils.ai_client import call_ai

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("/")
def summarize(payload: SummarizeInput):
    lang = payload.language or "code"

    system_prompt = (
        "You are a code analyst. Summarize code clearly and concisely."
    )

    user_prompt = (
        f"Summarize the following {lang} code:\n\n"
        f"{payload.code}\n\n"
        "Include: purpose, logic flow, key variables, edge cases."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return call_ai(messages, max_tokens=400)

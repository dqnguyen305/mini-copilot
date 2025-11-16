from fastapi import APIRouter
from models.schemas import FixCodeInput
from utils.ai_client import call_ai

router = APIRouter(prefix="/fix-code", tags=["fix-code"])

@router.post("/")
def fix_code(payload: FixCodeInput):
    lang = payload.language or "code"
    err = payload.error_message or "No error message provided."

    system_prompt = (
        "You are a senior software engineer. Fix the code, explain bugs, "
        "and suggest improvements."
    )

    user_prompt = (
        f"Language: {lang}\n\n"
        f"Original code:\n{payload.code}\n\n"
        f"Error message:\n{err}\n\n"
        "Tasks:\n"
        "1. Provide fixed code.\n"
        "2. Explain what was wrong.\n"
        "3. Suggest improvements.\n"
        "Return results in sections: Fixed Code, Explanation, Improvements."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return call_ai(messages, max_tokens=600)

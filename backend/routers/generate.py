from fastapi import APIRouter
from models.schemas import GenerateInput
from utils.ai_client import call_ai

router = APIRouter(prefix="/generate", tags=["generate"])

@router.post("/")
def generate(payload: GenerateInput):
    lang = payload.language or "any"
    framework = payload.framework or "any"

    system_prompt = (
        "You are an AI code generator. Produce clean, production-quality code."
    )

    user_prompt = (
        f"Description: {payload.description}\n\n"
        f"Language: {lang}\n"
        f"Framework: {framework}\n\n"
        "Requirements:\n"
        "- Output only code inside a single code block.\n"
        "- Use correct syntax.\n"
        "- Include helpful comments.\n"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return call_ai(messages, max_tokens=800)

from pydantic import BaseModel
from typing import Optional


class CodeInput(BaseModel):
    code: str
    language: Optional[str] = None


class FixCodeInput(BaseModel):
    code: str
    error_message: Optional[str] = None
    language: Optional[str] = None


class SummarizeInput(BaseModel):
    code: str
    language: Optional[str] = None


class GenerateInput(BaseModel):
    description: str
    language: Optional[str] = None
    framework: Optional[str] = None

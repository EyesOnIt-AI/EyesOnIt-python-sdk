from pydantic import BaseModel
from typing import Optional


class EOIPrompt(BaseModel):
    text: str
    threshold: Optional[int] = None
    background_prompt: bool = False

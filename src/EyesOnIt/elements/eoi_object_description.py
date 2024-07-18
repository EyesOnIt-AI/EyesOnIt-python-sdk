from pydantic import BaseModel
from typing import Optional


class EOIObjectDescription(BaseModel):
    text: str
    threshold: Optional[int] = None
    background_prompt: bool = False

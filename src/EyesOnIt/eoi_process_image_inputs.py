from typing import List
from pydantic import BaseModel
from .elements.eoi_region import EOIRegion
from .elements.eoi_prompt import EOIPrompt


class EOIProcessImageInputs(BaseModel):
    prompts: List[EOIPrompt]
    regions: List[EOIRegion]
    file: str

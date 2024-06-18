from typing import List
from pydantic import BaseModel
from data.elements.eoi_region import EOIRegion
from data.elements.eoi_prompt import EOIPrompt


class EOIProcessImageInputs(BaseModel):
    prompts: List[EOIPrompt]
    regions: List[EOIRegion]
    file: str

from typing import List
from pydantic import BaseModel
from .elements.eoi_region import EOIRegion
from .elements.eoi_object_description import EOIObjectDescription


class EOIProcessImageInputs(BaseModel):
    prompts: List[EOIObjectDescription]
    regions: List[EOIRegion]
    object_size: int
    file: str

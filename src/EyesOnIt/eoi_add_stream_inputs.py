from typing import List
from typing import Optional
from pydantic import BaseModel
from .elements.eoi_alerting import EOIAlerting
from .elements.eoi_bounding_box import EOIBoundingBox
from .elements.eoi_efficient_detection import EOIEfficientDetection
from .elements.eoi_prompt import EOIPrompt
from .elements.eoi_region import EOIRegion


class EOIAddStreamInputs(BaseModel):
    stream_url: str
    name: Optional[str] = None
    frame_rate: int = 5
    prompts: List[EOIPrompt]
    regions: List[EOIRegion]
    alerting: EOIAlerting
    efficient_detection: EOIEfficientDetection = EOIEfficientDetection()
    bounding_box: EOIBoundingBox = EOIBoundingBox()

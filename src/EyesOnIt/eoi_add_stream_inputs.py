from typing import List
from typing import Optional
from pydantic import BaseModel
from .elements.eoi_alerting import EOIAlerting
from .elements.eoi_bounding_box import EOIBoundingBox
from .elements.eoi_motion_detection import EOIMotionDetection
from .elements.eoi_object_description import EOIObjectDescription
from .elements.eoi_region import EOIRegion


class EOIAddStreamInputs(BaseModel):
    stream_url: str
    name: Optional[str] = None
    regions: List[EOIRegion]
    object_size: int = 100
    prompts: List[EOIObjectDescription]
    alerting: EOIAlerting
    efficient_detection: EOIMotionDetection = EOIMotionDetection()
    bounding_box: EOIBoundingBox = EOIBoundingBox()
    frame_rate: int = 5

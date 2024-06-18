from pydantic import BaseModel


class EOIEfficientDetection(BaseModel):
    periodic_check_enabled: bool = False
    periodic_check_seconds: float = 3.0
    motion_detection_enabled: bool = False
    motion_detection_threshold: int = 200
    motion_detection_seconds: float = 0.5

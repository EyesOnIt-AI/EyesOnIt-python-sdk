from pydantic import BaseModel
from typing import Optional


class EOIMonitorStreamInputs(BaseModel):
    stream_url: str
    duration_seconds: Optional[float] = None

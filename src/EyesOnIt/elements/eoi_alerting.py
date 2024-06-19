from .eoi_genetec import EOIGenetec
from pydantic import BaseModel
from typing import Optional


class EOIAlerting(BaseModel):
    alert_seconds_count: float = 0.1
    reset_seconds_count: float = 0.1
    phone_number: Optional[str] = None
    image_notification: bool = False
    genetec: EOIGenetec = EOIGenetec()


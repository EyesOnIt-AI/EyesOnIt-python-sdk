from pydantic import BaseModel
from typing import Optional


class EOIGenetecAlerting(BaseModel):
    webhook_event_id: Optional[int] = None
    webhook_camera_uuid: Optional[str] = None

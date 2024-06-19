from pydantic import BaseModel


class EOIStreamUrlInput(BaseModel):
    stream_url: str

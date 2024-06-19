from pydantic import BaseModel


class EOIRegion(BaseModel):
    top_left_x: int
    top_left_y: int
    width: int
    height: int

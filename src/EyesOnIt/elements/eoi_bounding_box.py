from pydantic import BaseModel


class EOIBoundingBox(BaseModel):
    bounding_box_enabled: bool = False
    detect_people: bool = False
    detect_vehicles: bool = False
    detect_bags: bool = False
    person_confidence_threshold: int = 30
    vehicle_confidence_threshold: int = 30
    bag_confidence_threshold: int = 30

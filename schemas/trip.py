from pydantic import BaseModel
from typing import Optional


class Trip(BaseModel):
    purpose: str
    travel_date: str
    duration_days: int
    accommodation: str
    sponsor: Optional[str] = None
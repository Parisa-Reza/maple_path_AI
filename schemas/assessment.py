from pydantic import BaseModel


class Assessment(BaseModel):
    eligibility: str = "Pending"
    confidence: float = 0.0
    reasoning: str = ""
from pydantic import BaseModel


class Recommendation(BaseModel):
    decision: str = "Pending"
    reason: str = ""
    reviewer: str = "AI"
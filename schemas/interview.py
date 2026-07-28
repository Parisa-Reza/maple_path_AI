from pydantic import BaseModel
from typing import List


class Interview(BaseModel):
    questions: List[str] = []
    answers: List[str] = []
    summary: str = ""
from pydantic import BaseModel
from typing import Optional


class Document(BaseModel):
    passport_file: Optional[str] = None
    bank_statement: Optional[str] = None
    employment_letter: Optional[str] = None
    invitation_letter: Optional[str] = None
    itinerary: Optional[str] = None
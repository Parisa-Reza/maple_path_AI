from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


class Application(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    applicant_name: str

    passport_number: str

    nationality: str

    purpose_of_visit: str

    status: str = "draft"
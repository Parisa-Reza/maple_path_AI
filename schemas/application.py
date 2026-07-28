from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Optional

from schemas.applicant import Applicant
from schemas.trip import Trip
from schemas.document import Document
from schemas.assessment import Assessment
from schemas.interview import Interview
from schemas.recommendation import Recommendation


class Application(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    applicant: Optional[Applicant] = None

    trip: Optional[Trip] = None

    documents: Optional[Document] = None

    assessment: Optional[Assessment] = None

    interview: Optional[Interview] = None

    recommendation: Optional[Recommendation] = None

    status: str = "Draft"
from pydantic import BaseModel


class Applicant(BaseModel):
    """
    Applicant's personal information.
    """

    name: str

    nationality: str

    passport_number: str

    occupation: str

    marital_status: str
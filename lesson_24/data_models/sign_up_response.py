from pydantic import BaseModel


class DataModel(BaseModel):
    userId: int
    distanceUnits: str
    currency: str

class SignUpResponseModel(BaseModel):
    status: str
    data: DataModel



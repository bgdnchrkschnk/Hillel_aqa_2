from pydantic import BaseModel


class DataModel(BaseModel):
    userId: int
    distanceUnits: str
    currency: str

class SignInResponseModel(BaseModel):
    status: str
    data: DataModel
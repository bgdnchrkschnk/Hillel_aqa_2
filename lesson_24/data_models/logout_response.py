from pydantic import BaseModel


class LogoutResponseModel(BaseModel):
    status: str
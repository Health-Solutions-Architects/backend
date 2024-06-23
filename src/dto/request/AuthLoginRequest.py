from pydantic import BaseModel


class AuthLoginRequest(BaseModel):
    email: str
    password: str

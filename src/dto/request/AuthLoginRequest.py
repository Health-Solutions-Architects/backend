from pydantic import BaseModel


class AuthLoginRequest(BaseModel):
    username_or_email: str
    password: str

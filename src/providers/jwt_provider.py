from datetime import datetime, timedelta
from typing import Type

import jwt
import orjson
from pydantic import BaseModel

from src.domain.models import UsuarioModel


class JwtProvider:
    # secret key
    secret: str
    # expiration time in minutes
    expiration: int
    # algorithms
    algorithms: str

    def __init__(self, secret: str, expiration: int, algorithms: str):
        self.secret = secret
        self.expiration = expiration
        self.algorithms = algorithms

    def encode(self, payload: dict) -> str:
        payload['exp'] = datetime.utcnow() + timedelta(hours=self.expiration)
        return jwt.encode(payload, self.secret, self.algorithms)

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret, self.algorithms)


class JwtPayload(BaseModel):
    sub: int
    email: str
    permissions: list[str]

    @classmethod
    def from_user(cls, usuario: Type[UsuarioModel], ) -> dict:
        return JwtPayload(
            sub=usuario.id,
            email=usuario.email,
            permissions=orjson.loads(usuario.permissoes.__str__())).model_dump()

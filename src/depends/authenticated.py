from fastapi.requests import Request
from fastapi.security import SecurityScopes
from pydantic import BaseModel

from src.depends.jwt_provider import DependsJwtProvider
from src.exceptions import HTTPExceptionUnauthorized


class AuthSession(BaseModel):
    user_id: int
    scopes: list[str]


def authenticated_user(request: Request, security_scopes: SecurityScopes, jwt: DependsJwtProvider):
    session = request.headers.get('x-auth')
    if not session:
        raise HTTPExceptionUnauthorized()

    jwt_payload = jwt.decode(token=session)

    return jwt_payload

from fastapi.requests import Request
from fastapi.security import SecurityScopes

from src.exceptions import HTTPExceptionUnauthorized


def authenticated_user(request: Request, security_scopes: SecurityScopes):
    session = request.cookies.get('session')
    if not session:
        raise HTTPExceptionUnauthorized()
    return dict(user_id=1)


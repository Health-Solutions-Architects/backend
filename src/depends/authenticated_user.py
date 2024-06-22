from fastapi.requests import Request
from fastapi.security import SecurityScopes

from src.exceptions import HTTPExceptionUnauthorized


def authenticated_user(request: Request, security_scopes: SecurityScopes):
    request.app.scopes = security_scopes.scopes
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPExceptionUnauthorized()
    print(security_scopes.scopes)
    print(security_scopes.scope_str)
    return dict(username='Ribeiro', password='12345')

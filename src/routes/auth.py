from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Security
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.depends.authenticated_user import authenticated_user
from src.models.user import User

router = APIRouter()

AuthenticatedUser = Annotated[User, Security(authenticated_user, scopes=['read', 'write'])]


@router.get('/login')
def login():
    return {'message': 'Login'}


@router.get('/login/auth')
def login_auth(
        request: Request,
        user: AuthenticatedUser):
    return {'message': 'Autenticado', 'user': user, 'scopes': request.app.scopes}


@router.get('/login/cookies')
def login_cookies():
    response = JSONResponse(content={'message': 'Sessão atualizada com sucesso!'}, status_code=200)
    response.set_cookie(key='access_token', value='access_token', max_age=60, expires=60)
    return response

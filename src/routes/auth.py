from fastapi import APIRouter
from fastapi.params import Security
from fastapi.responses import ORJSONResponse

from src.depends import (
    DatabaseSession, DependsAppSettings, DependsJwtProvider, authenticated_user
)
from src.domain.repository.auth_repository import AuthRepository
from src.dto.request.AuthLoginRequest import AuthLoginRequest
from src.providers import PasswordProvider
from src.providers.response import HttpResponse

router = APIRouter()


@router.post("/auth/login")
def post_auth_login(content: AuthLoginRequest,
                    session: DatabaseSession,
                    jwt_provider: DependsJwtProvider,
                    settings: DependsAppSettings):
    repository = AuthRepository(session=session)

    user = repository.find(email=content.username_or_email)
    if not user:
        return HttpResponse.message(status_code=400, message='Usuário e/ou Senha inválidos.')

    if not PasswordProvider.verify_password(password=content.password, hashed_password=user.senha):
        return HttpResponse.message(status_code=400, message='Usuário e/ou Senha inválidos.')

    response = ORJSONResponse({'message': 'Usuario autentica com sucesso!',
                               'data': dict(user_id=1)})

    user_jwt = jwt_provider.encode(dict(user_id=user.id, email=content.username_or_email))
    response.set_cookie(settings.session_key, user_jwt, httponly=True)
    return response


@router.get('/auth/logout')
def get_auth_logout(settings: DependsAppSettings):
    response = ORJSONResponse(content={'message': 'Deslogado com sucesso!'})
    response.delete_cookie(settings.session_key)
    return response


@router.get('/auth/user')
def get_auth_user(user=Security(authenticated_user, scopes=['login'])):
    return HttpResponse.ok(data={'message': 'Liberado', 'user': user})

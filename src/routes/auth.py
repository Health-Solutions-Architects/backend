from fastapi import APIRouter

from src.depends import DatabaseSession, DependsPasswordProvider
from src.domain.repository.auth_repository import AuthRepository
from src.dto.request.AuthLoginRequest import AuthLoginRequest
from src.providers.response import HttpResponse

router = APIRouter()


@router.post("/auth/login")
def post_auth(content: AuthLoginRequest, session: DatabaseSession, password_provider: DependsPasswordProvider):
    repository = AuthRepository(session=session)

    user = repository.find(email=content.username_or_email)
    if not user:
        return HttpResponse.message(status_code=400, message='Usuário e/ou Senha inválidos.')

    if not password_provider.verify_password(password=content.password, hashed_password=user.password):
        return HttpResponse.message(status_code=400, message='Usuário e/ou Senha inválidos.')

    # Setar os cookies junto com o jwt
    return HttpResponse.ok(data={"ok": True})

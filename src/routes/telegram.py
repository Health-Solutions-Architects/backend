from fastapi import APIRouter

from src.depends import DatabaseSession
from src.domain.repository.telegram_repository import PacienteRepository
from src.helpers.normalizadores import is_valid_cpf
from src.providers import HttpResponse

router = APIRouter()


@router.get('/telegram/user/{cpf}')
def get_telegram_user(cpf: str, session: DatabaseSession):
    repository = PacienteRepository(session=session)

    if not is_valid_cpf(cpf=cpf):
        return not HttpResponse.not_found()

    result = repository.find_paciente(cpf=cpf)
    if not result:
        return HttpResponse.not_found()

    return dict(user='Matheus')

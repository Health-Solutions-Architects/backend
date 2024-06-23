from fastapi import APIRouter
from fastapi.params import Security

from src.depends import DatabaseSession, authenticated_user
from src.domain.repository.fila_repository import FilaRepository
from src.helpers.basic_mapper import str_nivel_risco, str_nivel_prioridade
from src.providers import HttpResponse

router = APIRouter()


@router.get('/fila')
def get_fila(session: DatabaseSession, _=Security(authenticated_user, scopes=['fila:read'])):
    repository = FilaRepository(session)
    result = repository.get_all()
    map_result = [dict(fila_id=fila_id,
                       nome=nome,
                       nivel=str_nivel_risco(nivel),
                       prioridade=str_nivel_prioridade(prioridade)) for fila_id, nome, nivel, prioridade in result]
    return HttpResponse.ok(data={'message': 'Fila de Atendimento', 'data': map_result})

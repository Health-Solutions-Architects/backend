from fastapi import APIRouter
from fastapi.params import Security
from fastapi.requests import Request

from src.depends import authenticated_user
from src.depends.redis import DependsRedis
from src.depends.session_database import DatabaseSession
from src.domain.models import TriagemModel, FilaModel
from src.domain.repository.triagem_repository import TriagemRepository
from src.helpers.redis_keys import RedisKeys
from src.providers import HttpResponse

router = APIRouter()


@router.post('/triagem')
async def post_triagem(request: Request, session: DatabaseSession, cache: DependsRedis,
                       _=Security(authenticated_user, scopes=['triagem:create'])):
    try:
        repository = TriagemRepository(session)
        body_json = await request.json()

        paciente = repository.get_paciente(cpf=body_json.get('cpf'))
        if not paciente:
            paciente = repository.create_paciente(triagem_json=body_json)

        triagem = TriagemModel(
            cpf=paciente.cpf,
            nome=paciente.nome,
            data_nascimento=paciente.data_nascimento,
            sexo=body_json.get('sexo'),
            peso=body_json.get('peso'),
            altura=body_json.get('altura'),
            oximetria=body_json.get('oximetria'),
            pressao=body_json.get('pressao'),
            temperatura=body_json.get('temperatura'),
            parecer_tecnico=body_json.get('parecer'),
            nivel_risco=int(body_json['classificacao']),
            nivel_prioridade=int(body_json['prioridade']),
            paciente_id=paciente.id
        )

        session.add(triagem)
        session.commit()
        session.refresh(triagem)

        fila = FilaModel(
            nivel_risco=triagem.nivel_risco,
            nivel_prioridade=triagem.nivel_prioridade,
            status='ESPERA',
            paciente_id=triagem.paciente_id,
            triagem_id=triagem.id
        )

        session.add(fila)
        session.commit()
        session.refresh(fila)

        chave_pre_triagem = RedisKeys.PRE_TRIAGEM.format(cpf=triagem.cpf)
        cache.delete(chave_pre_triagem)
    except:
        session.rollback()

    return HttpResponse.ok(data={'message': 'Atendimento criado com sucesso, enviado para a fila'})

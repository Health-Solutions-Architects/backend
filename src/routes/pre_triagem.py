import orjson
from fastapi import APIRouter
from fastapi.params import Security

from src.depends import DependsRedis, authenticated_user, DatabaseSession
from src.domain.repository.pre_triagem_repository import PreTriagemRepository
from src.dto.request.pre_atendimento_request import PreAtendimentoRequest
from src.helpers.gpt_assistant import get_assistant_classification
from src.helpers.redis_keys import RedisKeys
from src.providers import HttpResponse

router = APIRouter()


@router.get('/pre-triagem/{cpf}')
def get_pre_triagem(cpf: str, cache: DependsRedis, _=Security(authenticated_user, scopes=['pre_triagem:read'])):
    chave_pre_triagem = RedisKeys.PRE_TRIAGEM.format(cpf=cpf)
    result = cache.get(name=chave_pre_triagem)
    if not result:
        return HttpResponse.not_found(data={'message': 'Pre Triagem não encontrada'})
    result_json = orjson.loads(result)
    return HttpResponse.ok(data={'message': 'Pre Triagem encontrada', 'data': result_json})


@router.get('/pre-triagem/{cpf}/paciente')
def get_pre_triagem_paciente(cpf: str, session: DatabaseSession):
    repository = PreTriagemRepository(session)
    result = repository.get_paciente_name(cpf=cpf)
    if not result:
        return HttpResponse.not_found()
    return HttpResponse.ok(data={'message': 'Paciente encontrado',
                                 'data': {'nome': result}})


@router.post('/pre-triagem')
def post_pre_triagem(content: PreAtendimentoRequest, cache: DependsRedis):
    chave_pre_triagem = RedisKeys.PRE_TRIAGEM.format(cpf=content.cpf)

    if cache.exists(chave_pre_triagem):
        dados_triagem = cache.get(chave_pre_triagem)
        response_data = {
            'message': 'Pre atendimento ja registrado no sistema',
            'dados': orjson.loads(dados_triagem)}
        return HttpResponse.create(400, response_data)

    response_gpt = get_assistant_classification(dados=content.model_dump())

    save_data = content.model_dump()
    save_data.update({'response_gpt': response_gpt})

    cache.set(name=chave_pre_triagem, value=orjson.dumps(save_data, default=str).decode(), ex=86400)

    return HttpResponse.ok(data={"message": 'Pre Atendimento registrado com sucesso, dirija-se a unidade de saude.',
                                 'data': response_gpt})

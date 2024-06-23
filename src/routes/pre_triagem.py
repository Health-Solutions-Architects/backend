import orjson
from fastapi import APIRouter

from src.depends import DependsRedis
from src.dto.request.pre_atendimento_request import PreAtendimentoRequest
from src.helpers.gpt_assistant import get_assistant_classification
from src.providers import HttpResponse

router = APIRouter()


@router.post('/pre-triagem')
def post_pre_triagem(content: PreAtendimentoRequest, cache: DependsRedis):
    chave_pre_triagem = f'atendimento:{content.cpf}'

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

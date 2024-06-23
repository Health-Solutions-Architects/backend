from pydantic import BaseModel


class PreAtendimentoRequest(BaseModel):
    cpf: str
    nome: str
    data_nascimento: str
    peso: float
    altura: float
    sintomas: str

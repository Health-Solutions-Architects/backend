import datetime

from pydantic import BaseModel


class PacienteEntity(BaseModel):
    id: int
    cpf: str
    nome: str
    data_nascmento: datetime

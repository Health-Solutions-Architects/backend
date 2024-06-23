from datetime import datetime
from typing import Literal

import orjson
from sqlalchemy import Column, String, BigInteger, Enum, ForeignKey, DateTime, JSON

from src.database.database import Base

TipoUsuario = Enum('ADMINISTRADOR', 'PACIENTE', 'FUNCIONARIO', name='tipo_usuario', create_type=False)

TypeTipoUsuario = Literal['ADMINISTRADOR', 'PACIENTE', 'FUNCIONARIO']


class UsuarioModel(Base):
    __tablename__ = 'usuarios'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    tipo_usuario = Column(TipoUsuario, nullable=False)
    permissoes = Column(JSON, nullable=False)

    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

    paciente_id = Column(BigInteger, ForeignKey('pacientes.id'))
    funcionario_id = Column(BigInteger, ForeignKey('funcionarios.id'))

    @classmethod
    def create(cls, email: str, senha: str, tipo_usuario: TypeTipoUsuario, permissoes: list[str]) -> 'UsuarioModel':
        return UsuarioModel(email=email,
                            senha=senha,
                            tipo_usuario=tipo_usuario,
                            permissoes=orjson.dumps(permissoes).decode())

from datetime import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, Date, String, Double, DateTime, Integer

from src.database.database import Base


class TriagemModel(Base):
    __tablename__ = 'triagens'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    cpf = Column(String)
    nome = Column(String)
    data_nascimento = Column(Date)
    sexo = Column(String)

    peso = Column(String)
    altura = Column(String)

    oximetria = Column(String)
    pressao = Column(String)
    temperatura = Column(String)

    parecer_tecnico = Column(String)
    nivel_risco = Column(Integer)
    nivel_prioridade = Column(Integer)

    data_criacao = Column(DateTime, default=datetime.now)

    paciente_id = Column(BigInteger, ForeignKey('pacientes.id'))
    funcionario_id = Column(BigInteger, ForeignKey('funcionarios.id'))

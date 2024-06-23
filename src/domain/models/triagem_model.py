from datetime import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, Date, String, Double, DateTime

from src.database.database import Base


class TriagemModel(Base):
    __tablename__ = 'triagens'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    cpf = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(String, nullable=False)

    peso = Column(Double, nullable=False)
    altura = Column(Double, nullable=False)

    oximetria = Column(String, nullable=False)
    pressao = Column(String, nullable=False)
    temperatura = Column(Double, nullable=False)
    parecer_tecnico = Column(String, nullable=False)

    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

    paciente_id = Column(BigInteger, ForeignKey('pacientes.id'), nullable=False)
    funcionario_id = Column(BigInteger, ForeignKey('funcionarios.id'), nullable=False)

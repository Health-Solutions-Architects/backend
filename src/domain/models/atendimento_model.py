from datetime import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, DateTime

from src.database.database import Base


class AtendimentoModel(Base):
    __tablename__ = 'atendimentos'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

    atendimento_ref = Column(BigInteger, ForeignKey('atendimentos.id'), nullable=False)

    paciente_id = Column(BigInteger, ForeignKey('pacientes.id'), nullable=False)
    funcionario_id = Column(BigInteger, ForeignKey('funcionarios.id'), nullable=False)
    triagem_id = Column(BigInteger, ForeignKey('triagens.id'), nullable=False)

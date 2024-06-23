from datetime import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, DateTime

from src.database.database import Base


class FilaModel(Base):
    __tablename__ = 'fila'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    status = Column(String, nullable=False)

    nivel_risco = Column(Integer, nullable=False)
    nivel_prioridade = Column(Integer, nullable=False)

    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

    paciente_id = Column(BigInteger, ForeignKey('pacientes.id'), nullable=False)
    triagem_id = Column(BigInteger, ForeignKey('triagens.id'), nullable=False)

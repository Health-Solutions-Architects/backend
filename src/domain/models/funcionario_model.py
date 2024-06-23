from datetime import datetime

from sqlalchemy import Column, String, BigInteger, Date, DateTime

from src.database.database import Base


class FuncionarioModel(Base):
    __tablename__ = 'funcionarios'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    cpf = Column(String(length=11), nullable=False, unique=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)

    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

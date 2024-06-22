from sqlalchemy import Column, String, BigInteger

from src.database.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    cpf = Column(String)

from typing import Type

from sqlalchemy.orm import Session

from src.domain.models import UsuarioModel


class AuthRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def find(self, email: str) -> Type[UsuarioModel]:
        return self.session.query(UsuarioModel).filter_by(email=email).first()

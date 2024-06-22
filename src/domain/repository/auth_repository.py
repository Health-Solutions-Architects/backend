from typing import Type

from sqlalchemy.orm import Session

from src.domain.models.user_model import UserModel


class AuthRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def find(self, email: str) -> Type[UserModel]:
        return self.session.query(UserModel).filter_by(email=email).first()

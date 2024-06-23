from typing import Type

from sqlalchemy.orm import Session

from src.domain.models.paciente_model import PacienteModel


class PacienteRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def find_paciente(self, cpf: str) -> Type[PacienteModel]:
        return self.session.query(PacienteModel).filter_by(cpf=cpf).first()

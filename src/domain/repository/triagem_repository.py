from datetime import datetime
from typing import Type

from sqlalchemy.orm import Session

from src.domain.models import PacienteModel


class TriagemRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get_paciente(self, cpf=str) -> Type[PacienteModel]:
        return self.session.query(PacienteModel).filter_by(cpf=cpf).first()

    def create_paciente(self, triagem_json: dict) -> PacienteModel:
        paciente = PacienteModel(
            cpf=triagem_json['cpf'],
            nome=triagem_json['nome'],
            data_nascimento=datetime.strptime(triagem_json['data_nascimento'].split('T')[0],
                                              '%Y-%m-%d').date()
        )
        self.session.add(paciente)
        self.session.commit()
        self.session.refresh(paciente)
        return paciente

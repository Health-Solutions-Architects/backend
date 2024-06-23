from sqlalchemy.orm import Session

from src.domain.models import PacienteModel


class PreTriagemRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get_paciente_name(self, cpf=str) -> str | None:
        result = self.session.query(PacienteModel).filter_by(cpf=cpf).first()
        if not result:
            return None
        return result.nome.__str__()

from sqlalchemy.orm import Session

from src.domain.models import PacienteModel
from src.domain.models.fila_model import FilaModel


class FilaRepository:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return (self.session.query(FilaModel.id, PacienteModel.nome, FilaModel.nivel_risco, FilaModel.nivel_prioridade)
                .join(PacienteModel, PacienteModel.id == FilaModel.paciente_id)
                .order_by(FilaModel.nivel_risco, FilaModel.nivel_prioridade)
                .all())

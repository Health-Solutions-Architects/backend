from datetime import datetime

from src.database.database import Base, engine, SessionLocal
from src.domain.models import *
from src.providers import PasswordProvider


def main():
    Base.metadata.reflect(bind=engine)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    sessao = SessionLocal()

    usuario_administrador = UsuarioModel.create(email='administrador@hackasaude.com',
                                                senha=PasswordProvider.hash_password('administrador'),
                                                tipo_usuario='ADMINISTRADOR')

    sessao.add(usuario_administrador)
    sessao.commit()
    sessao.flush()

    paciente = PacienteModel(
        cpf="12345678901",
        nome="João da Silva",
        data_nascimento=datetime.strptime('10/05/2001', '%d/%m/%Y').date()
    )

    usuario_paciente = UsuarioModel.create(email='paciente@hackasaude.com',
                                           senha=PasswordProvider.hash_password('paciente'),
                                           tipo_usuario='PACIENTE')

    sessao.add(paciente)
    sessao.commit()
    sessao.refresh(paciente)

    usuario_paciente.paciente_id = paciente.id
    sessao.add(usuario_paciente)
    sessao.commit()
    sessao.flush()

    funcionario = FuncionarioModel(
        cpf="41499426097",
        nome="Cauã Victor Teixeira",
        data_nascimento=datetime.strptime('14/04/1959', '%d/%m/%Y').date()
    )

    usuario_funcionario = UsuarioModel.create(email='funcionario@hackasaude.com',
                                              senha=PasswordProvider.hash_password('funcionario'),
                                              tipo_usuario='FUNCIONARIO')

    sessao.add(funcionario)
    sessao.commit()
    sessao.refresh(funcionario)

    usuario_funcionario.funcionario_id = funcionario.id
    sessao.add(usuario_funcionario)
    sessao.commit()
    sessao.flush()

    sessao.close()


if __name__ == '__main__':
    main()

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
                                                tipo_usuario='ADMINISTRADOR',
                                                permissoes=['administrador'])

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
                                           tipo_usuario='PACIENTE',
                                           permissoes=['paciente'])

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
                                              tipo_usuario='FUNCIONARIO',
                                              permissoes=['funcionario'])

    sessao.add(funcionario)
    sessao.commit()
    sessao.refresh(funcionario)

    usuario_funcionario.funcionario_id = funcionario.id
    sessao.add(usuario_funcionario)
    sessao.commit()
    sessao.flush()

    paciente1 = PacienteModel(
        cpf="14658418304",
        nome="Bryan Oliver Renato Lopes",
        data_nascimento=datetime.strptime('15/01/2001', '%d/%m/%Y').date()
    )

    sessao.add(paciente1)
    sessao.commit()
    sessao.refresh(paciente1)

    triagem1 = TriagemModel(
        cpf=paciente1.cpf,
        nome=paciente1.nome,
        data_nascimento=paciente1.data_nascimento,
        sexo='M',
        peso=60.5,
        altura=1.78,
        oximetria='90%',
        pressao=12.8,
        temperatura=37,
        parecer_tecnico='Bixo ta suave',
        nivel_risco=1,
        nivel_prioridade=2,
        funcionario_id=funcionario.id,
        paciente_id=paciente1.id
    )

    sessao.add(triagem1)
    sessao.commit()
    sessao.refresh(triagem1)

    fila1 = FilaModel(
        status='ESPERA',
        nivel_risco=triagem1.nivel_risco,
        nivel_prioridade=triagem1.nivel_prioridade,
        paciente_id=paciente1.id,
        triagem_id=triagem1.id
    )

    sessao.add(fila1)
    sessao.commit()

    paciente2 = PacienteModel(
        cpf="19447573258",
        nome="Eduardo Samuel Felipe Rezende",
        data_nascimento=datetime.strptime('08/05/2006', '%d/%m/%Y').date()
    )

    sessao.add(paciente2)
    sessao.commit()
    sessao.refresh(paciente2)

    triagem2 = TriagemModel(
        cpf=paciente2.cpf,
        nome=paciente2.nome,
        data_nascimento=paciente2.data_nascimento,
        sexo='M',
        peso=60.5,
        altura=1.78,
        oximetria='90%',
        pressao=12.8,
        temperatura=37,
        parecer_tecnico='Bixo ta grave e peferencial',
        nivel_risco=1,
        nivel_prioridade=1,
        funcionario_id=funcionario.id,
        paciente_id=paciente2.id
    )

    sessao.add(triagem2)
    sessao.commit()
    sessao.refresh(triagem2)

    fila2 = FilaModel(
        status='ESPERA',
        nivel_risco=triagem2.nivel_risco,
        nivel_prioridade=triagem2.nivel_prioridade,
        paciente_id=paciente2.id,
        triagem_id=triagem2.id
    )

    sessao.add(fila2)
    sessao.commit()

    paciente3 = PacienteModel(
        cpf="92386038122",
        nome="Murilo Sebastião Erick Fernandes",
        data_nascimento=datetime.strptime('08/02/2002', '%d/%m/%Y').date()
    )

    sessao.add(paciente3)
    sessao.commit()
    sessao.refresh(paciente3)

    triagem3 = TriagemModel(
        cpf=paciente3.cpf,
        nome=paciente3.nome,
        data_nascimento=paciente3.data_nascimento,
        sexo='M',
        peso=60.5,
        altura=1.78,
        oximetria='90%',
        pressao=12.8,
        temperatura=37,
        parecer_tecnico='Nivel 2 Prioridade 2',
        nivel_risco=2,
        nivel_prioridade=2,
        funcionario_id=funcionario.id,
        paciente_id=paciente3.id
    )

    sessao.add(triagem3)
    sessao.commit()
    sessao.refresh(triagem3)

    fila3 = FilaModel(
        status='ESPERA',
        nivel_risco=triagem3.nivel_risco,
        nivel_prioridade=triagem3.nivel_prioridade,
        paciente_id=paciente3.id,
        triagem_id=triagem3.id
    )

    sessao.add(fila3)
    sessao.commit()

    # uotro

    paciente4 = PacienteModel(
        cpf="15297545501",
        nome="Theo Matheus Fogaça",
        data_nascimento=datetime.strptime('15/01/2001', '%d/%m/%Y').date()
    )

    sessao.add(paciente4)
    sessao.commit()
    sessao.refresh(paciente4)

    triagem4 = TriagemModel(
        cpf=paciente4.cpf,
        nome=paciente4.nome,
        data_nascimento=paciente4.data_nascimento,
        sexo='M',
        peso=60.5,
        altura=1.78,
        oximetria='90%',
        pressao=12.8,
        temperatura=37,
        parecer_tecnico='Nivel 2 prioridade 1',
        nivel_risco=2,
        nivel_prioridade=1,
        funcionario_id=funcionario.id,
        paciente_id=paciente4.id
    )

    sessao.add(triagem4)
    sessao.commit()
    sessao.refresh(triagem4)

    fila4 = FilaModel(
        status='ESPERA',
        nivel_risco=triagem4.nivel_risco,
        nivel_prioridade=triagem4.nivel_prioridade,
        paciente_id=paciente4.id,
        triagem_id=triagem4.id
    )

    sessao.add(fila4)
    sessao.commit()

    sessao.close()


if __name__ == '__main__':
    main()

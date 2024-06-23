import re

from validate_docbr import CPF

_SOMENTE_NUMEROS = re.compile(r'\d+')


def is_valid_cpf(cpf: str) -> bool:
    return CPF().validate(cpf)


def normalizar_cpf(cpf: str):
    return _SOMENTE_NUMEROS.sub('', cpf)

def str_nivel_risco(value: int):
    return {
        1: 'vermelho',
        2: 'laranja',
        3: 'amarelo',
        4: 'verde',
        5: 'azul',
    }[value]


def str_nivel_prioridade(value: int):
    return {
        1: 'preferencial',
        2: 'normal',
    }[value]

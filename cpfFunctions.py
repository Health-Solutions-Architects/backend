def cadastrarCpf(cpf: str)-> bool:
    return True

def verificaCpf(cpf: str)-> bool:
    return True


def captura_email(message, bot):
    email = message.text
    bot.reply_to(message, 'CPF registrado. Agora, por favor, informe seu Email:')
    bot.register_next_step_handler(message, captura_nome, email, bot)

def captura_nome(message, email, bot):
    nome = message.text
    bot.reply_to(message, 'Email registrado. Agora, por favor, informe sua idade:')
    bot.register_next_step_handler(message, captura_idade, email, nome, bot)

def captura_idade(message, email, nome, bot):
    idade = message.text
    if idade.isdigit():
        bot.reply_to(message, 'Idade registrada. Agora, por favor, informe os sintomas que está sentindo:')
        bot.register_next_step_handler(message, captura_sintomas, email, nome, idade, bot)
    else:
        bot.reply_to(message, 'Idade inválida. Por favor, informe sua idade em números:')
        bot.register_next_step_handler(message, captura_idade, email, nome, bot)

def captura_sintomas(message, email, nome, idade, bot):
    sintomas = message.text
    # Aqui você pode adicionar a lógica para processar as informações capturadas
    bot.reply_to(message, f'Registro completo:\nEmail: {email}\nNome: {nome}\nIdade: {idade}\nSintomas: {sintomas}')
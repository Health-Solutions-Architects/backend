import telebot
import re
import cpfFunctions
from telebot import types

bot = telebot.TeleBot('')  # Insira o token do seu bot aqui
pattern = r'[\d]{11}'


@bot.message_handler(commands=['iniciar'])
def inicio(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    quest_sim = types.InlineKeyboardButton('Sim', callback_data='prefix:possui-cadastro')
    quest_nao = types.InlineKeyboardButton('Não', callback_data='prefix:nao-possui-cadastro')
    
    markup.add(quest_sim, quest_nao)
    bot.send_message(message.chat.id, 'Você possui cadastro?', reply_markup=markup)


@bot.message_handler(commands=['triagem'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    quest_1 = types.InlineKeyboardButton('Pronto Atendimento / Triagem', callback_data='prefix:pronto-atendimento')
    quest_2 = types.InlineKeyboardButton('Agendamento e Consultas', callback_data='prefix:agendamento-consultas')
    quest_3 = types.InlineKeyboardButton('Telemedicina', callback_data='prefix:telemedicina')
    quest_4 = types.InlineKeyboardButton('Dashboard de Fluxo', callback_data='prefix:dashboard-fluxo')

    markup.add(quest_1, quest_2, quest_3, quest_4)

    bot.send_message(message.chat.id, 'Escolha uma opção:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'prefix:possui-cadastro')
def pegaCpf(callback):
    bot.send_message(callback.message.chat.id, 'Informe seu CPF')


@bot.message_handler(func=lambda message: re.match(pattern, message.text))
def verifica_cpf(message):
    verificado = cpfFunctions.verificaCpf(message.text)
    if verificado:
        bot.reply_to(message, 'CPF verificado com sucesso. Por favor, informe seu email:')
        bot.register_next_step_handler(message, captura_email)
    else:
        bot.reply_to(message, 'CPF não encontrado. Por favor, verifique e tente novamente.')

def captura_email(message):
    email = message.text
    # Aqui você pode adicionar a lógica para validar o email, se necessário
    bot.reply_to(message, 'Email registrado. Agora, por favor, informe seu nome:')
    bot.register_next_step_handler(message, captura_nome, email)

def captura_nome(message, email):
    nome = message.text
    bot.reply_to(message, 'Nome registrado. Agora, por favor, informe sua idade:')
    bot.register_next_step_handler(message, captura_idade, email, nome)

def captura_idade(message, email, nome):
    idade = message.text
    if idade.isdigit():
        bot.reply_to(message, 'Idade registrada. Agora, por favor, informe os sintomas que está sentindo:')
        bot.register_next_step_handler(message, captura_sintomas, email, nome, idade)
    else:
        bot.reply_to(message, 'Idade inválida. Por favor, informe sua idade em números:')
        bot.register_next_step_handler(message, captura_idade, email, nome)

def captura_sintomas(message, email, nome, idade):
    sintomas = message.text
    # Aqui você pode adicionar a lógica para processar as informações capturadas
    bot.reply_to(message, f'Registro completo:\nEmail: {email}\nNome: {nome}\nIdade: {idade}\nSintomas: {sintomas}')


@bot.message_handler(func=lambda message: True)
def fallback_message(message):
    bot.reply_to(message, 'Desculpe, não entendi sua mensagem. Tente usar os comandos disponíveis.')


if __name__ == "__main__":
    print("Bot está rodando no link \nLink está em https://web.telegram.org/k/#@UclTestesTCC_bot")
    bot.polling()

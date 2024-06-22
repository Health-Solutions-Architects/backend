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

@bot.callback_query_handler(func=lambda call: call.data == 'prefix:nao-possui-cadastro')
def naoPossuiCadastro(message):
    bot.send_message(message.message.chat.id, 'Informe seu CPF')
    bot.register_next_step_handler(message.message, cpfFunctions.captura_email, bot)

@bot.callback_query_handler(func=lambda call: call.data == 'prefix:possui-cadastro')
def possuiCadastro(message):
    bot.send_message(message.message.chat.id, 'Informe seu CPF')
    if cpfFunctions.verificaCpf(message.message.text):
        bot.register_next_step_handler(message.message, sistema_de_triagem)

@bot.message_handler(commands=['triagem'])
def sistema_de_triagem(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    quest_1 = types.InlineKeyboardButton('Pronto Atendimento / Triagem', callback_data='prefix:pronto-atendimento')
    quest_2 = types.InlineKeyboardButton('Agendamento e Consultas', callback_data='prefix:agendamento-consultas')
    quest_3 = types.InlineKeyboardButton('Telemedicina', callback_data='prefix:telemedicina')
    quest_4 = types.InlineKeyboardButton('Dashboard de Fluxo', callback_data='prefix:dashboard-fluxo')

    markup.add(quest_1, quest_2, quest_3, quest_4)

    bot.send_message(message.chat.id, 'Escolha uma opção:', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def fallback_message(message):
    bot.reply_to(message, 'Desculpe, não entendi sua mensagem. Tente usar os comandos disponíveis.\n /iniciar ou /triagem ')


if __name__ == "__main__":
    print("Bot está rodando no link \nLink está em https://web.telegram.org/k/#@UclTestesTCC_bot")
    bot.polling()

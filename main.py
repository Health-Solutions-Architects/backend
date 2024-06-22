#pip install pyTelegramBotAPI
import telebot
from telebot import types

bot = telebot.TeleBot()
@bot.message_handler(commands=['quiz'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    pergunta1 = types.InlineKeyboardButton('Pergunta1 ', callback_data='Resposta 1')
    pergunta2 = types.InlineKeyboardButton('Pergunta2 ', callback_data='Resposta 2')
    pergunta3 = types.InlineKeyboardButton('Pergunta3 ', callback_data='Resposta 3')
    pergunta4 = types.InlineKeyboardButton('Pergunta4 ', callback_data='Resposta 4')

    markup.add(pergunta1, pergunta2, pergunta3, pergunta4)

    bot.send_message(message.chat.id, 'meu teste', reply_markup=markup)
    
@bot.callback_query_handler(func= lambda call: True)
def answer(callback):
    if callback.message:
        bot.send_message(callback.message.chat.id, 'AAAAAAAAAA')

if __name__ == "__main__":
    print("Bot está rodando...")
    bot.polling()
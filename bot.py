import sys
from telebot import TeleBot

from emoticons import emote_keyboard, emote_dict

bot_token = sys.argv[1]
bot = TeleBot(token=bot_token)


@bot.message_handler(commands=['search'])
def search_query(message):
    key = message.text[message.text.find(' ') + 1:]
    print(key)
    if key in emote_dict:
        bot.send_message(message.chat.id, emote_dict[key])
    else:
        bot.send_message(message.chat.id, 'found nothing :(')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')
    bot.send_message(message.chat.id, "Tap what you want!", reply_markup=emote_keyboard)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


print('bot server started.')
bot.polling()

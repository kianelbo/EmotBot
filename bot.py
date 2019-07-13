import os
import telebot
from flask import Flask, request

from emoticons import emote_keyboard, emote_dict, get_inline_results

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


@bot.inline_handler(lambda query: True)
def send_inline(inline_query):
    try:
        results = get_inline_results(inline_query.query)
        bot.answer_inline_query(inline_query.id, results)
    except Exception as e:
        print(e)


@bot.message_handler(commands=['search'])
def search_emote(message):
    key = message.text[message.text.find(' ') + 1:]
    if key in emote_dict:
        bot.send_message(message.chat.id, emote_dict[key])
    else:
        bot.send_message(message.chat.id, 'found nothing :(')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "All you need to do is tap!", reply_markup=emote_keyboard)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text not in emote_dict.values():
        bot.send_message(message.chat.id, 'unknown command :/', reply_markup=emote_keyboard)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://emotbot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

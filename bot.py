import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, Filters, InlineQueryHandler, MessageHandler, Updater

from emoticons import emotes_dict


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = os.environ['TOKEN']


buttons = [InlineKeyboardButton(emote) for emote in emotes_dict.values()]
keyboard = [buttons[x:x+3] for x in range(0, len(buttons), 3)]
reply_markup = InlineKeyboardMarkup(keyboard)

all_emote_results = [
    InlineQueryResultArticle(i, emote, InputTextMessageContent(emote)) for i, emote in enumerate(emotes_dict.values())
]


def inline_query(update, context):
    query = update.inline_query.query

    if query in emotes_dict:
        result = [InlineQueryResultArticle('1', emotes_dict[query], InputTextMessageContent(emotes_dict[query]))]
    else:
        result = all_emote_results

    update.inline_query.answer(result)

def start(update, context):
    update.message.reply_text("Just tap on the one you need!", reply_markup=reply_markup)

def search(update, context):
    query = update.message.text
    key = query[query.find(' ') + 1:]
    if key in emotes_dict:
        update.message.reply_text(emotes_dict[key])
    else:
        update.message.reply_text("found nothing :(")

def non_command(update, context):
    update.message.reply_text("unknown command :/", reply_markup=reply_markup)

def errors(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(InlineQueryHandler(inline_query))
    dp.add_handler(CommandHandler("search", search))
    dp.add_handler(MessageHandler(Filters.text, non_command))
    dp.add_error_handler(errors)

    updater.start_webhook(listen="0.0.0.0", port=int(os.environ.get('PORT', 8443)), url_path=TOKEN)
    updater.bot.setWebhook('https://emotbot.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == "__main__":
    main()

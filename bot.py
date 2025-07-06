import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, filters, InlineQueryHandler, MessageHandler

from emoticons import emotes_dict


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = os.environ['BOT_TOKEN']
URL = os.environ['WEBHOOK_BASE_URL']
PORT = int(os.environ.get('PORT', 5000))


buttons = [InlineKeyboardButton(emote, switch_inline_query=emote) for emote in emotes_dict.values()]
keyboard = [buttons[x : x + 3] for x in range(0, len(buttons), 3)]
reply_markup = InlineKeyboardMarkup(keyboard)

all_emote_results = [
    InlineQueryResultArticle(i, emote, InputTextMessageContent(emote)) for i, emote in enumerate(emotes_dict.values())
]


async def inline_query(update, context):
    query = update.inline_query.query

    if query in emotes_dict:
        result = [InlineQueryResultArticle('1', emotes_dict[query], InputTextMessageContent(emotes_dict[query]))]
    else:
        result = all_emote_results

    await update.inline_query.answer(result)

async def start(update, context):
    await update.message.reply_text("Just tap on the one you need!", reply_markup=reply_markup)

async def search(update, context):
    query = update.message.text
    key = query[query.find(' ') + 1:]
    resp = emotes_dict[key] if key in emotes_dict else "found nothing :("
    await update.message.reply_text(resp)

async def non_command(update, context):
    await update.message.reply_text("unknown command :/", reply_markup=reply_markup)

async def errors(update, context):
    await logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inline_query))
    application.add_handler(CommandHandler("search", search))
    application.add_handler(MessageHandler(filters.TEXT, non_command))
    application.add_error_handler(errors)

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=URL + TOKEN,
    )

if __name__ == "__main__":
    main()

from  telegram import Update
from telegram.ext import CommandHandler, Application, MessageHandler, filters 
from decouple import config

from get_license.get_license import command_handler, get_license
from homework_handler.get_homework import send_homework

TOKEN = config("TELEGRAM_TOKEN")
URL_SERVER = config("SERVER_TOKEN")

def main():

    app = Application.builder().token(TOKEN ).build()
    app.add_handler(CommandHandler("start", command_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_license))
    app.add_handler(MessageHandler(filters.PHOTO, send_homework))
    app.run_polling(allowed_updates=Update.ALL_TYPES)
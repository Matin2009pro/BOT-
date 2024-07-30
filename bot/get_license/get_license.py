from  telegram import Update
from telegram.ext import ContextTypes
from decouple import config

from requests_manager.requests_methode import *
from text import *

URL_SERVER = config("SERVER_TOKEN")



#command start handler
async def command_handler(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    json = get_json(URL_SERVER, {'chat_id': chat_id})
    if json:
        pass
    else:
        await context.bot.send_message(chat_id=chat_id, text=text_get_license)




#function get license and send to server
async def get_license(update:Update, context:ContextTypes.DEFAULT_TYPE):
    license = update.effective_message.text
    chat_id = update.effective_chat.id
    json = get_json(URL_SERVER, {'chat_id': chat_id})
    if json:
        pass
    else:
        data = {'license': license, 'chat_id': chat_id}
        reponse = post_license(URL_SERVER, data=data)
        if reponse:
            await context.bot.send_message(chat_id=chat_id, text=text_receive_license)
        else:
            await context.bot.send_message(chat_id=chat_id, text=text_cant_receive_license)
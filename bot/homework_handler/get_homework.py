from  telegram import Update
from telegram.ext import ContextTypes
from decouple import config
import os
from requests_manager.requests_methode import post_file
from text import *

URL_SERVER = config("SERVER_TOKEN")

#function get homework photo and send to server
async def send_homework(update:Update, context:ContextTypes.DEFAULT_TYPE):
    #download photo 
    chat_id = update.effective_chat.id
    photo_file = await context.bot.getFile(update.effective_message.photo[-1].file_id)
    file_name = os.path.join("DOWNLOAD_PHOTO", f"photo_{update.effective_message.id}.jpg")
    await photo_file.download_to_drive(file_name)
    
    #send photo to server
    data = {'chat_id': chat_id}
    file = {'file' : file_name}
    reponse = post_file(URL_SERVER, data, file)
    os.remove(rf"DOWNLOAD_PHOTO\photo_{update.effective_message.id}.jpg")

    #answer to homework
    if reponse:
        await context.bot.send_message(chat_id=chat_id, text=text_receive_homework)
        await context.bot.send_message(chat_id=chat_id, text=reponse.text)
    else:
        await context.bot.send_message(chat_id=chat_id, text=text_cant_receive_homework)
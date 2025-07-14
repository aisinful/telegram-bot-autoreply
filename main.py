import os
from telegram.ext import Updater, MessageHandler, Filters

def auto_reply(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hola! Gracias por mandarme un mensaje 💕 Por desgracia recibo demasiados mensajes por aqui, si quieres hablar conmigo puedes contactarme en mi Fansly u Only link.me/kalullamas")

def main():
    token = os.getenv("7871592696:AAFwxP5QCfx6HFDmnAS_38DmR3tFvEEIY3k")
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Gracias por mandarme un mensaje 💕 Por desgracia recibo demasiados mensajes por aqui, si quieres hablar conmigo puedes contactarme en mi Fansly u Only link.me/kalullamas")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    app.run_polling()

if __name__ == '__main__':
    main()
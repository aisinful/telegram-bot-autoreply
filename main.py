import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Gracias por mandarme un mensaje 💕 Por desgracia recibo demasiados mensajes por aquí. "
        "Si quieres hablar conmigo, puedes contactarme en mi Fansly u Only link.me/kalullamas"
    )

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN no definido")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # Mantener el bot vivo
    while True:
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
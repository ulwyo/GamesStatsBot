import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!")

async def get_stats_dota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!")


if __name__ == '__main__':
    application = ApplicationBuilder().token("8468363471:AAF9gTEsQFGVXON9eF0akWi2vBXj-NK2sOY").build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()

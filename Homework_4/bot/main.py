TOKEN = '6714990097:AAHcQjprc_VMYp1CWo2NDSo0tgCxo7W4no4'

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Привет, я бот, поговори со мной!
    
    Команды:
    /approve
    """)


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.chat.username, update.message.chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    <strong>Вы подписаны на обновления!</strong>
    """, parse_mode = "html")

# async def keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data="1"),
#             InlineKeyboardButton("Option 2", callback_data="2"),
#         ],
#         [InlineKeyboardButton("Option 3", callback_data="3")],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="Вы нажали на кнопку!",
#         reply_markup=reply_markup
#     )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('approve', approve))

    print("bot started")
    application.run_polling()
    print("bot stopped")

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.environ.get("BOT_TOKEN")

TEXT = (
    "🧠 *Тест Клифтона (Gallup)*\n\n"
    "Психолог потратил 40 лет, чтобы доказать:\n"
    "у каждого есть 5 талантов с рождения\n\n"
    "Мои топ-5:\n"
    "1 — Футурист\n"
    "2 — Стратег\n"
    "3 — Интеллект\n"
    "4 — Эмпатия\n"
    "5 — Максимизатор\n\n"
    "Пройди и напиши свой результат 👇"
)

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🎯 Пройти тест", url="https://high5test.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(TEXT, parse_mode="Markdown", reply_markup=reply_markup)

def test(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🎯 Пройти тест", url="https://high5test.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(TEXT, parse_mode="Markdown", reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("test", test))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

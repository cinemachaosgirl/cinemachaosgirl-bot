import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎯 Пройти тест", url="https://high5test.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(TEXT, parse_mode="Markdown", reply_markup=reply_markup)

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎯 Пройти тест", url="https://high5test.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(TEXT, parse_mode="Markdown", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))
    app.run_polling()

import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Read bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("❓ Ask a Question", callback_data='ask')],
        [InlineKeyboardButton("📝 Daily Quiz", callback_data='quiz')],
        [InlineKeyboardButton("🏆 Challenge Friends", callback_data='challenge')],
        [InlineKeyboardButton("🛠 Tools", callback_data='tools')],
        [InlineKeyboardButton("📊 My Score", callback_data='score')],
        [InlineKeyboardButton("ℹ️ About", callback_data='about')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Hi! I'm Study Buddy — your AI-powered study companion.\n"
        "Ask questions, take quizzes, challenge friends and more!\n\n"
        "What would you like to do?",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE

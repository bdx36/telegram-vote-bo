import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 VIPLINK71 Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "👋 স্বাগতম VIPLINK71 বটে! 💐\n\n"
        "আমাদের প্রিমিয়াম গ্রুপে এক্সক্লুসিভ ভিডিও, ফাইল ও চ্যাট একসেস পেতে নিচের বাটনে ক্লিক করুন।\n\n"
        "4 বাটনে ক্লিক করার পর \"Open Link\" চাপুন।"
    )
    keyboard = [[InlineKeyboardButton("Buy Group 🔥", url="https://viplink71.com/home")]]
    await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

def start_bot():
    async def runner():
        app_bot = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
        app_bot.add_handler(CommandHandler("start", start))
        await app_bot.run_polling()
    asyncio.run(runner())

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

from pyrogram import Client, filters
from datetime import datetime
import json

api_id = 23765081
api_hash = "d5bf55b4bc9d9aa6e41a9719497b5c0f"
bot_token = "7818868232:AAEhGeLljnk96p_owTzWIVynH1eEqnLWMas"

app = Client("CryptoNotifierPro", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    welcome_text = f"""
🚀 Welcome {user.first_name}!
I'm CryptoNotifierPro – your all-in-one trading assistant.

✅ Crypto + Stock Alerts
📘 Strategy PDFs
📊 Trade Setups + Chart View
🔐 VIP Access & Referral Rewards
🧠 Trading Psychology Alerts
🧮 Lot Size & Trailing SL Calculators
🗓️ Daily Trade Calendar + Setup Archive
🏆 Score Badges + Quizzes
👥 Customer Support + Admin Panel

Use /help or the menu below to explore features.
"""
    await message.reply(welcome_text)

@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """🟦 Use /start to begin.
Use commands like /price BTC, /buyvip, /refer, /watchlist, /strategy, /support etc.
Explore sections: Crypto 📈 | Stock 🏛 | Learn 📘 | Free 🚀 | VIP 🔐
"""
    await message.reply(help_text)

app.run()
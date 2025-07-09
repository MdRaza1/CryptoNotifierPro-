# CryptoNotifierPro Final Bot (Simplified Placeholder)

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
📊 Trade Setups  
🔐 VIP Access & Referral Rewards  
🤖 24x7 Customer Support

Use the menu below or type /help to explore features.
"""
    await message.reply(welcome_text)


@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """🟦 Use /start to begin.
Use the buttons or type commands like /price BTC, /buyvip, /refer, etc."""
    await message.reply(help_text)


app.run()

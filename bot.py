
from pyrogram import Client, filters
from datetime import datetime
from fastapi import FastAPI, Request
import threading
import uvicorn
import json
import asyncio

from config import api_id, api_hash, bot_token

app_bot = Client("CryptoNotifierPro", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
fast = FastAPI()

# /start command
@app_bot.on_message(filters.command("start"))
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

# /help command
@app_bot.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """🟦 Use /start to begin.
Use commands like /price BTC, /buyvip, /refer, /watchlist, /strategy, /support etc.
Explore sections: Crypto 📈 | Stock 🏛️ | Learn 📘 | Free 🚀 | VIP 🔐
"""
    await message.reply(help_text)

# FastAPI root route
@fast.get("/")
async def root():
    return {"status": "ok", "message": "CryptoNotifierPro API is live"}

# Run bot and FastAPI in parallel threads
def run_bot():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    app_bot.run()

def run_server():
    uvicorn.run(fast, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_server).start()

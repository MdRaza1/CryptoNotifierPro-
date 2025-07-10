# Full-featured bot.py for Render deployment via GitHub
import asyncio, threading, os
from pyrogram import Client, filters
from fastapi import FastAPI
from config import api_id, api_hash, bot_token
from referral_system import handle_referral
from payment_gateway import handle_payment
from support_bot import support_handler
from strategy_pdf import send_strategy_pdf
from trading_tools import trading_tools_handler
from vip_system import check_vip_status
from watchlist_module import manage_watchlist
from daily_calendar import get_calendar
from quiz_module import handle_quiz
from admin_panel import admin_handler

app_bot = Client("CryptoNotifierPro", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
fast = FastAPI()

@app_bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Welcome to CryptoNotifierPro\nUse /help to explore features.")

@app_bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply("📘 Use /price, /buyvip, /refer, /strategy, /watchlist, /support")

@fast.get("/")
async def root():
    return {"status": "ok", "message": "CryptoNotifierPro API is running"}

def run_bot():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    app_bot.run()

def run_server():
    import uvicorn
    uvicorn.run(fast, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_server).start()

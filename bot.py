
from pyrogram import Client, filters
from fastapi import FastAPI, Request
import uvicorn
import threading
import asyncio
from config import api_id, api_hash, bot_token

# Import all handlers/modules
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

# Start command
@app_bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    welcome = f"""
👋 Welcome {user.first_name}!

🚀 I’m CryptoNotifierPro – Your Ultimate Trading Assistant Bot!

📈 Crypto • 📊 Stocks • 🎯 Strategies • 🔐 VIP Tools

Type /help to view all features or explore via buttons.
"""
    await message.reply(welcome)

# Help command
@app_bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply(
        "📘 Commands:\n"
        "/price BTC | /buyvip | /refer | /strategy | /watchlist\n"
        "/calendar | /quiz | /support | /vip | /free | /admin"
    )

# Add handlers
app_bot.add_handler(filters.command("refer")(handle_referral))
app_bot.add_handler(filters.command("buyvip")(handle_payment))
app_bot.add_handler(filters.command("support")(support_handler))
app_bot.add_handler(filters.command("strategy")(send_strategy_pdf))
app_bot.add_handler(filters.command("watchlist")(manage_watchlist))
app_bot.add_handler(filters.command("calendar")(get_calendar))
app_bot.add_handler(filters.command("quiz")(handle_quiz))
app_bot.add_handler(filters.command("admin")(admin_handler))

@fast.get("/")
async def home():
    return {"status": "running", "bot": "CryptoNotifierPro"}

# Threaded bot and FastAPI run
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

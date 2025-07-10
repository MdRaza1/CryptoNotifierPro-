from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading, uvicorn
from fastapi import FastAPI, Request

import config, vip_system, referral_system, payment_gateway, support_bot, strategy_pdf, watchlist_module

app_bot = Client("CryptoBot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📉 Crypto", callback_data="menu_crypto"),
         InlineKeyboardButton("🏛 Stock", callback_data="menu_stock")],
        [InlineKeyboardButton("📘 Learn", callback_data="menu_learn"),
         InlineKeyboardButton("🚀 Free", callback_data="menu_free"),
         InlineKeyboardButton("🔐 VIP", callback_data="menu_vip")],
    ])

@app_bot.on_message(filters.command("start"))
async def start(c, m):
    await m.reply(f"🚀 Hello {m.from_user.first_name}! Welcome to your ultimate trading bot.", reply_markup=main_menu())

@app_bot.on_message(filters.command("help"))
async def help_cmd(c, m):
    await m.reply("/price BTC – coin price\n/buyvip – Get VIP\n/refer – Referral link\n/strategy – PDF list\n/watchlist – Manage alerts\n/support – Contact support", reply_markup=main_menu())

@app_bot.on_message(filters.command("price"))
async def price_cmd(c, m):
    sym = m.text.split(maxsplit=1)[1].upper() if len(m.text.split())>1 else None
    if not sym: return await m.reply("Usage: /price BTC")
    price = strategy_pdf.fetch_price(sym)
    await m.reply(f"Current price of {sym}: ₹{price}")

@app_bot.on_message(filters.command("buyvip"))
async def buyvip_cmd(c, m):
    msg = await m.reply("Generating your VIP payment link...")
    url = payment_gateway.create_link(m.from_user.id)
    await msg.edit(f"💳 Pay for VIP: {url}")

@app_bot.on_message(filters.command("refer"))
async def refer_cmd(c, m):
    link = referral_system.get_link(m.from_user.id)
    await m.reply(f"Your referral link:\n{link}")

@app_bot.on_message(filters.command("strategy"))
async def strat_cmd(c, m):
    pdfs = strategy_pdf.list_pdfs()
    await m.reply("Available strategy PDFs:\n" + "\n".join(pdfs))

@app_bot.on_message(filters.command("watchlist"))
async def watch_cmd(c, m):
    cur = watchlist_module.get_list(m.from_user.id)
    await m.reply("Your watchlist:\n" + "\n".join(cur) if cur else "Your watchlist is empty.")

@app_bot.on_message(filters.command("support"))
async def sup_cmd(c, m):
    await m.reply(support_bot.get_info())

@app_bot.on_callback_query()
async def cb(c, cbq):
    data = cbq.data
    actions = {
        "menu_crypto": "🚀 Crypto section coming soon!",
        "menu_stock": "🏙️ Stock market section coming soon!",
        "menu_learn": "📘 Learn trading strategies step-by-step!",
        "menu_free": "🚀 You're on Free plan. Upgrade anytime.",
        "menu_vip": "🔐 VIP gives full tools, calculator, alerts!"
    }
    await cbq.message.edit(actions.get(data, "Unknown menu"), reply_markup=main_menu())

# Start webhook server for Instamojo
fast = FastAPI()

@fast.post("/instamojo-webhook")
async def im_webhook(request: Request):
    data = await request.form()
    valid = payment_gateway.validate(data)
    if valid:
        uid, plan = payment_gateway.process(data)
        await app_bot.send_message(uid, f"🎉 Payment confirmed! Your VIP ({plan}) is now active.")
    return {"status":"ok"}

import asyncio
import threading

def run_bot():
    try:
        loop =
asyncio.get_running_loop()
    except RuntimeError:
        loop =
asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    app_bot.run()

def run_server():
    uvicorn.run(fast, host="0.0.0.0", port=8000)

    if __name__ == "__main__":
    
    threading.Thread(target=run_bot).start()

    threading.Thread(target=run_server).start()
    
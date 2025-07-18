import asyncio
import threading
import os
from pyrogram import Client, filters
from fastapi import FastAPI

from config import api_id, api_hash, bot_token

from crypto_alerts import handle_crypto_alerts
from coin_converter import convert_coin
from crypto_news import send_crypto_news

from stock_prediction import handle_stock_prediction
from stock_timing_assistant import stock_timing
from multi_timeframe import multi_timeframe_analysis
from daily_stock_report import send_daily_stock_summary

from strategy_pdf_sender import send_strategy_pdf
from lot_size_calc import calculate_lot_size
from psychology_alert import send_psych_alert
from setup_archive import save_setup_result
from performance_badge import give_performance_badge
from trailing_sl import trailing_stoploss
from multi_target import multi_target_alert
from quiz_module import quiz_command

from vip_system import check_vip_status
from referral_system import handle_referral
from reward_tracker import check_referral_rewards
from payment_gateway import handle_payment
from vip_expiry_checker import check_and_expire_vip

from support_bot import support_handler
from admin_panel import admin_handler
from watchlist_module import manage_watchlist
from daily_calendar import get_calendar

from button_layout import get_main_keyboard
from welcome_handler import send_welcome
from help_command import show_help

from topcoin_tracker import auto_sector_tracker
from journal_module import position_journal_handler
from risk_analysis import risk_analyzer
from psychology_alerts import stop_warning_handler
from stock_calendar import stock_calendar_handler
from swing_module import swing_analysis_handler
from setup_archive import setup_archive_handler

app_bot = Client("CryptoNotifierPro", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

fast = FastAPI()

@fast.get("/")
async def root():
    return {"status": "running", "message": "CryptoNotifierPro API is live"}

@app_bot.on_message(filters.command("start"))
async def start(client, message):
    await send_welcome(client, message)

@app_bot.on_message(filters.command("help"))
async def help(client, message):
    await show_help(client, message)

@app_bot.on_message(filters.command("price"))
async def price(client, message):
    await handle_crypto_alerts(client, message)

@app_bot.on_message(filters.command("convert"))
async def convert(client, message):
    await convert_coin(client, message)

@app_bot.on_message(filters.command("news"))
async def news(client, message):
    await send_crypto_news(client, message)

@app_bot.on_message(filters.command("predict"))
async def predict(client, message):
    await handle_stock_prediction(client, message)

@app_bot.on_message(filters.command("timing"))
async def timing(client, message):
    await stock_timing(client, message)

@app_bot.on_message(filters.command("mta"))
async def mta(client, message):
    await multi_timeframe_analysis(client, message)

@app_bot.on_message(filters.command("dailyreport"))
async def report(client, message):
    await send_daily_stock_summary(client, message)

@app_bot.on_message(filters.command("strategy"))
async def strategy(client, message):
    await send_strategy_pdf(client, message)

@app_bot.on_message(filters.command("lotcalc"))
async def lotcalc(client, message):
    try:
        args = message.text.split()[1:]
        if len(args) != 3:
            raise ValueError("Invalid format")

        capital = float(args[0])
        risk_percent = float(args[1])
        stop_loss = float(args[2])

        from lot_size_calc import calculate_lot_size
        result = calculate_lot_size(capital, risk_percent, stop_loss)
        await message.reply(result)

    except:
        await message.reply("❗ Use format: /lotcalc 10000 1 5\n(capital risk_percent stop_loss)")

@app_bot.on_message(filters.command("psych"))
async def psych(client, message):
    await send_psych_alert(client, message)

@app_bot.on_message(filters.command("result"))
async def result(client, message):
    await save_setup_result(client, message)

@app_bot.on_message(filters.command("badge"))
async def badge(client, message):
    await give_performance_badge(client, message)

@app_bot.on_message(filters.command("trail"))
async def trail(client, message):
    try:
        args = message.text.split()[1:]
        if len(args) != 3:
            raise ValueError("Invalid arguments")

        entry = float(args[0])
        current = float(args[1])
        trail_percent = float(args[2])

        result = get_trailing_sl(entry, current, trail_percent)
        await message.reply(result)

    except Exception as e:
        await message.reply("❗ Use format: /trail 100 95 2\n(entry current trail%)")

@app_bot.on_message(filters.command("target"))
async def target(client, message):
    await multi_target_alert(client, message)

@app_bot.on_message(filters.command("quiz"))
async def quiz(client, message):
    await quiz_command(client, message)

@app_bot.on_message(filters.command("vip"))
async def vip(client, message):
    await check_vip_status(client, message)

@app_bot.on_message(filters.command("refer"))
async def refer(client, message):
    await handle_referral(client, message)

@app_bot.on_message(filters.command("rewards"))
async def rewards(client, message):
    await check_referral_rewards(client, message)

@app_bot.on_message(filters.command("buyvip"))
async def buyvip(client, message):
    await handle_payment(client, message)

@app_bot.on_message(filters.command("support"))
async def support(client, message):
    await support_handler(client, message)

@app_bot.on_message(filters.command("admin"))
async def admin(client, message):
    await admin_handler(client, message)

@app_bot.on_message(filters.command("watchlist"))
async def watchlist(client, message):
    await manage_watchlist(client, message)

@app_bot.on_message(filters.command("calendar"))
async def calendar(client, message):
    await get_calendar(client, message)

@app_bot.on_message(filters.command("topcoins"))
async def topcoins_handler(client, message):
    await auto_sector_tracker(client, message)

@app_bot.on_message(filters.command("journal"))
async def journal_handler(client, message):
    await position_journal_handler(client, message)

@app_bot.on_message(filters.command("risk"))
async def risk_handler(client, message):
    await risk_analyzer(client, message)

@app_bot.on_message(filters.command("reminder"))
async def reminder_handler(client, message):
    await stop_warning_handler(client, message)

@app_bot.on_message(filters.command("calendarstock"))
async def calendarstock_handler(client, message):
    await stock_calendar_handler(client, message)

@app_bot.on_message(filters.command("swing"))
async def swing_handler(client, message):
    await swing_analysis_handler(client, message)

@app_bot.on_message(filters.command("setup"))
async def setup_handler(client, message):
    await setup_archive_handler(client, message)

def run_bot():
    app_bot.run()

def run_vip_checker():
    check_and_expire_vip()

if name == "main":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_vip_checker).start()

    import uvicorn
    uvicorn.run("bot:fast", host="0.0.0.0", port=8000)
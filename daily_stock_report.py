# daily_stock_report.py
import datetime

async def send_daily_stock_summary(client, message):
    today = datetime.date.today().strftime("%d %b %Y")
    msg = f"""🗓️ Daily Stock Summary – {today}

🔹 NIFTY50: 19,820.55 (+0.34%)
🔹 BANKNIFTY: 45,120.00 (-0.12%)
🔹 Top Gainers: RELIANCE, TCS, INFY
🔹 Top Losers: HDFCBANK, ASIANPAINT, ITC

📍 News: Market opened flat. Midcaps showed strength. RBI policy awaited.
📊 Suggestion: Focus on breakouts with strong volume.

_(Disclaimer: Sample data. Enable live API for full automation)_"""
    await message.reply(msg)

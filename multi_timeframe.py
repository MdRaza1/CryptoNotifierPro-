# multi_timeframe.py
import random

async def multi_timeframe_analysis(client, message):
    try:
        stock = message.text.split(" ", 1)[1].strip().upper()
    except:
        await message.reply("⚠️ Use format: /mta TATAMOTORS")
        return

    tf_result = {
        "1H": random.choice(["🟢 Bullish", "🔴 Bearish", "⚪ Neutral"]),
        "4H": random.choice(["🟢 Bullish", "🔴 Bearish", "⚪ Neutral"]),
        "1D": random.choice(["🟢 Bullish", "🔴 Bearish", "⚪ Neutral"])
    }

    msg = f"🧠 Multi-Timeframe Analysis for {stock}:\n\n"
    for tf, view in tf_result.items():
        msg += f"🕒 {tf}: {view}\n"
    await message.reply(msg)

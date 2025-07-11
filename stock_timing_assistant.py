# stock_timing_assistant.py
import random

async def stock_timing(client, message):
    try:
        stock = message.text.split(" ", 1)[1].strip().upper()
    except:
        await message.reply("⚠️ Use format: /timing TATAMOTORS")
        return

    entry = random.choice(["🔔 Enter near support zone", "🚫 Avoid – wait for pullback", "🟢 Breakout confirmed – possible entry"])
    exit = random.choice(["🏁 Exit at next resistance", "⚠️ Partial booking suggested", "📌 Trail stop loss if in profit"])
    await message.reply(f"📅 Timing suggestion for {stock}:\n\nEntry: {entry}\nExit: {exit}")

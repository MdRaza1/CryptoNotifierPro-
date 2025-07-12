# advanced_education_module.py
from pyrogram import Client, filters
from pyrogram.types import Message
from vip_lesson_guard import guard_vip_access

advanced_lessons = {
    "candle": "🕯️ Candlestick Patterns\n\nHammer, Doji, Engulfing — watch for reversals and confirmation.",
    "trendline": "📈 Trendlines\n\nUse to mark support/resistance. Connect swing lows/highs.",
    "volume": "🔊 Volume Analysis\n\nVolume confirms the move. Spikes often signal breakouts.",
    "breakout": "🚀 Breakouts\n\nWhen price breaks key level with volume — strong trend may follow."
}

@Client.on_message(filters.command(["learn"]))
async def learn_advanced(client: Client, message: Message):
    if not await guard_vip_access(message):
        return

    args = message.text.split()
    if len(args) < 2:
        return await message.reply("Usage: /learn candle | trendline | volume | breakout")

    topic = args[1].lower()
    content = advanced_lessons.get(topic)
    if content:
        await message.reply(content)
    else:
        await message.reply("❌ Topic not found. Try: candle, trendline, volume, breakout")

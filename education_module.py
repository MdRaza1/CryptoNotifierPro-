# education_module.py
from pyrogram import Client, filters
from pyrogram.types import Message

# Basic trading lessons
lessons = {
    1: "📘 Lesson 1: What is the Stock Market?\n\nThe stock market is where buyers and sellers trade shares of public companies...",
    2: "📘 Lesson 2: What is a Candlestick?\n\nA candlestick shows open, close, high, and low prices for a specific time period.",
    3: "📘 Lesson 3: Types of Traders\n\nScalper, Day Trader, Swing Trader, Position Trader — different timeframes & goals.",
    4: "📘 Lesson 4: Support and Resistance\n\nSupport = price floor. Resistance = price ceiling.",
    5: "📘 Lesson 5: Risk Management\n\nOnly risk 1-2% per trade. Use stop loss. Stick to your plan."
}

@Client.on_message(filters.command("education"))
async def education_main(client: Client, message: Message):
    text = "📚 Trading Education Menu\n\nChoose a lesson:\n"
    for i in lessons:
        text += f"/lesson{i} - Lesson {i}\n"
    text += "\nUse /quiz to test your knowledge!"
    await message.reply(text)

# Dynamic lesson handlers
for i in lessons:
    async def send_lesson(client, message, i=i):
        await message.reply(lessons[i])
    Client.on_message(filters.command(f"lesson{i}"))(send_lesson)

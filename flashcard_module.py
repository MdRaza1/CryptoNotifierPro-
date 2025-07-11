# flashcard_module.py
from pyrogram import Client, filters
import random

flashcards = [
    {"q": "What is Volume?", "a": "Volume = number of trades happening. Higher volume = strong move."},
    {"q": "What is RSI?", "a": "RSI shows overbought or oversold zones. Above 70 = overbought."},
    {"q": "What is Risk-Reward Ratio?", "a": "It shows how much you risk to gain. Ideal RRR is 1:2 or more."},
    {"q": "Define Support", "a": "Support is a price level where buying interest is expected."}
]

@Client.on_message(filters.command("flashcard"))
async def flashcard_handler(client, message):
    card = random.choice(flashcards)
    await message.reply(f"📘 {card['q']}\n\n💡 {card['a']}")

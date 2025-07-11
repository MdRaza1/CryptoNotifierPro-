from pyrogram import Client, filters
from pyrogram.types import Message
from button_layout import get_main_keyboard

async def send_welcome(client: Client, message: Message):
    await message.reply(
        "🚀 Welcome to CryptoNotifierPro!\n\n"
        "🔍 I am your personal Trading Assistant Bot.\n\n"
        "Use the menu below to explore features.",
        reply_markup=get_main_keyboard()
    )

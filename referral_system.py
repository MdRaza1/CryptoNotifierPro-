# referral_system.py

from pyrogram.types import Message

async def handle_referral(client, message: Message):
    await message.reply("🎁 Your referral link is: https://t.me/CryptoNotifierPro_bot?start=ref123")
from pyrogram.types import Message

async def handle_referral(client, message: Message):
    await message.reply("🎁 Your referral link: https://t.me/CryptoNotifierPro_bot?start=ref123")

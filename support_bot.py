# support_bot.py

from pyrogram.types import Message

async def support_handler(client, message: Message):
    await message.reply("👨‍💻 Our 24x7 support will contact you soon. For now, send your query to @CryptoRaza0")
from pyrogram.types import Message

async def support_handler(client, message: Message):
    await message.reply("👨‍💻 Our support will reach out soon. DM @CryptoRaza0 for help.")

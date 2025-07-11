from pyrogram.types import Message

async def handle_payment(client, message: Message):
    await message.reply("💳 Payment verification system is active (test mode).")

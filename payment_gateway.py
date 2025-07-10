# payment_gateway.py

from pyrogram.types import Message

async def handle_payment(client, message: Message):
    await message.reply("💳 Payment system is under development. Please wait for updates.")
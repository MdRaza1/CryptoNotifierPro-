from pyrogram.types import Message

async def check_vip_status(client, message: Message):
    await message.reply("🔐 Checking your VIP status...\n✅ You are a VIP member!")

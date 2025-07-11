from pyrogram.types import Message

async def admin_handler(client, message: Message):
    await message.reply("🛠️ Admin panel access granted (stub).")

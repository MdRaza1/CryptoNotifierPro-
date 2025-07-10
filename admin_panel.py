# admin_panel.py

from pyrogram.types import Message

async def admin_handler(client, message: Message):
    await message.reply("🛠️ Admin panel feature is under development.")
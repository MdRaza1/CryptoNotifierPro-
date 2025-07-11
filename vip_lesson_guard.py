# vip_lesson_guard.py
from vip import is_user_vip
from pyrogram.types import Message

async def guard_vip_access(message: Message):
    user_id = message.from_user.id
    if not is_user_vip(user_id):
        await message.reply("🚫 This feature is only for VIPs. Use /buyvip to upgrade.")
        return False
    return True

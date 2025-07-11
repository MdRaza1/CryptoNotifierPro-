from pyrogram.types import Message

async def get_calendar(client, message: Message):
    await message.reply("📅 Here is your daily trade calendar. (Feature coming soon)")

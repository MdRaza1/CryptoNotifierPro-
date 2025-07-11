from pyrogram.types import Message

async def handle_quiz(client, message: Message):
    await message.reply("🧠 Mini quiz feature coming soon!")

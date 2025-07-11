from pyrogram.types import Message

async def trading_tools_handler(client, message: Message):
    await message.reply("🛠️ Use /lotcalc, /risk, /badge etc. Tools will be available soon.")

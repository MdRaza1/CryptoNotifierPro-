from pyrogram.types import Message

async def send_strategy_pdf(client, message: Message):
    await message.reply_document("https://example.com/sample-strategy.pdf", caption="📘 Here is your strategy guide.")

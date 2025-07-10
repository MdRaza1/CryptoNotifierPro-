# strategy_pdf.py

from pyrogram.types import Message

async def send_strategy_pdf(client, message: Message):
    await message.reply_document("https://example.com/your-strategy-pdf-link.pdf", caption="📘 Here is your trading strategy PDF.")
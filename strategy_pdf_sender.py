# strategy_pdf_sender.py
from pyrogram import Client, filters
from pyrogram.types import Message
from vip import is_user_vip

@Client.on_message(filters.command("strategy"))
async def send_strategy_pdf(client: Client, message: Message):
    user_id = message.from_user.id
    if not is_user_vip(user_id):
        return await message.reply("🚫 Only VIP members can access these strategy PDFs.")

    await message.reply_document("pdf/Intraday_Strategy.pdf", caption="📘 Intraday Strategy")
    await message.reply_document("pdf/Swing_Strategy.pdf", caption="📘 Swing Trading")
    await message.reply_document("pdf/Psychology_Guide.pdf", caption="🧠 Trading Psychology")

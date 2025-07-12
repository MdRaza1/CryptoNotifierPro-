# referral_system.py

from pyrogram import Client, filters
from pyrogram.types import Message

BASE_REF_LINK = "https://t.me/CryptoNotifierPro_bot?start="

async def handle_referral(client: Client, message: Message):
    user_id = message.from_user.id
    referral_link = f"{BASE_REF_LINK}{user_id}"
    await message.reply(
        f"🔗 Your Referral Link:\n{referral_link}\n\n"
        "Invite your friends and earn rewards based on their VIP purchases!"
    )

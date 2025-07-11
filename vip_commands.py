# vip_commands.py
from pyrogram import Client, filters
from vip import is_user_vip, add_vip, remove_vip, get_all_vips

ADMIN_ID = 7556144909  # Apna Telegram user ID

@Client.on_message(filters.command("vip"))
async def check_vip(client, message):
    if is_user_vip(message.from_user.id):
        await message.reply("✅ You are a VIP member!")
    else:
        await message.reply("❌ You are not a VIP.\nUse /buyvip to upgrade.")

@Client.on_message(filters.command("buyvip"))
async def buy_vip_info(client, message):
    await message.reply(
        "💎 VIP Plans:\n\n"
        "1 Month – ₹499\n"
        "3 Months – ₹1299\n"
        "6 Months – ₹2499\n"
        "Lifetime – ₹14999\n\n"
        "Use /pay to purchase VIP access."
    )

@Client.on_message(filters.command("addvip") & filters.user(7556144909))
async def add_vip_cmd(client, message):
    if len(message.command) < 3:
        return await message.reply("Usage: /addvip user_id days")
    user_id = message.command[1]
    days = int(message.command[2])
    date = add_vip(user_id, days)
    await message.reply(f"✅ User {user_id} is now VIP until {date}")

@Client.on_message(filters.command("removevip") & filters.user(7556144909))
async def remove_vip_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /removevip user_id")
    user_id = message.command[1]
    if remove_vip(user_id):
        await message.reply(f"❌ VIP removed from user {user_id}")
    else:
        await message.reply("⚠️ User not found in VIP list")

@Client.on_message(filters.command("viplist") & filters.user(7556144909))
async def list_vips(client, message):
    vips = get_all_vips()
    if not vips:
        return await message.reply("No VIP users yet.")
    text = "💎 VIP Users:\n" + "\n".join([f"{uid} → {expiry}" for uid, expiry in vips.items()])
    await message.reply(text)

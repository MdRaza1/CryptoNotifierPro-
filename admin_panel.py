from pyrogram import Client, filters
from pyrogram.types import Message
import json

# ✅ Replace with your Telegram user ID
ADMIN_ID = 7556144909

# ✅ File to store VIP members
VIP_FILE = "vip_members.json"

# Load VIP members
def load_vip():
    try:
        with open(VIP_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save VIP members
def save_vip(members):
    with open(VIP_FILE, "w") as f:
        json.dump(members, f, indent=2)

# 🗣 Broadcast to all users
@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message: Message):
    if not message.reply_to_message:
        await message.reply("❗ Reply to a message you want to broadcast.")
        return

    try:
        from config import all_users  # All registered user IDs
    except ImportError:
        await message.reply("⚠️ Unable to import user list from config.")
        return

    count = 0
    for user_id in all_users:
        try:
            await client.send_message(user_id, message.reply_to_message.text)
            count += 1
        except:
            continue

    await message.reply(f"✅ Broadcast sent to {count} users.")

# ➕ Add VIP
@Client.on_message(filters.command("addvip") & filters.user(ADMIN_ID))
async def add_vip(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: /addvip <user_id>")
        return

    user_id = int(message.command[1])
    members = load_vip()

    if user_id in members:
        await message.reply("🔁 User is already a VIP.")
    else:
        members.append(user_id)
        save_vip(members)
        await message.reply("✅ Added to VIP list.")

# ➖ Remove VIP
@Client.on_message(filters.command("removevip") & filters.user(ADMIN_ID))
async def remove_vip(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: /removevip <user_id>")
        return

    user_id = int(message.command[1])
    members = load_vip()

    if user_id in members:
        members.remove(user_id)
        save_vip(members)
        await message.reply("❌ Removed from VIP list.")
    else:
        await message.reply("🚫 User is not in VIP list.")

# 📊 User Stats
@Client.on_message(filters.command("userstats") & filters.user(ADMIN_ID))
async def user_stats(client, message: Message):
    try:
        from config import all_users
    except ImportError:
        await message.reply("⚠️ Couldn't fetch users from config.")
        return

    total = len(all_users)
    vip = load_vip()
    vip_count = len(vip)
    free = total - vip_count

    await message.reply(
        f"📊 User Stats\n\n👥 Total Users: {total}\n🔐 VIP Users: {vip_count}\n🆓 Free Users: {free}"
    )

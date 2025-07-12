from pyrogram import Client, filters
from pyrogram.types import Message

async def show_help(client: Client, message: Message):
    await message.reply(
        "🛠 Help Menu\n\n"
        "Use the following commands:\n"
        "/price - Get coin price\n"
        "/calendar - Check event calendar\n"
        "/convert - Currency conversion\n"
        "/quiz - Test your trading knowledge\n"
        "/education - Learn trading basics\n"
        "/referral - Your referral link\n"
        "/rewards - Your referral rewards\n"
        "\nMore coming soon!"
    )

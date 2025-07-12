# performance_badge.py

async def give_performance_badge(client, message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply("❗ Use format: /badge YourName - Achieved X% gain today")
        return

    achievement = text[1].strip()
    badge_message = f"🏅 Performance Badge 🏅\n\n{achievement}"
    await message.reply(badge_message)

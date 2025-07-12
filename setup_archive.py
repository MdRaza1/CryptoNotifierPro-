# setup_archive.py

archive_data = []

async def add_to_archive(setup):
    archive_data.append(setup)

async def view_archive():
    return "\n".join(archive_data) if archive_data else "📂 No trade setups saved yet."

# 👇 Yeh function neeche paste kar
async def save_setup_result(client, message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply("❗ Use format: /result SetupName - Success or /result SetupName - Fail")
        return

    setup = text[1].strip()
    archive_data.append(setup)
    await message.reply(f"📌 Setup result saved:\n\n{setup}")


# setup_archive.py
archive_data = []

async def add_to_archive(setup):
    archive_data.append(setup)

async def view_archive():
    return "\n".join(archive_data) if archive_data else "🗂️ No trade setups saved yet."

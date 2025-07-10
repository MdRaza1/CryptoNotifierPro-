
# config.py - for CryptoNotifierPro

from pyrogram import Client

# Telegram Bot Credentials
api_id = 23765081
api_hash = "d5bf55b4bc9d9aa6e41a9719497b5c0f"
bot_token = "7818868232:AAEhGeLljnk96p_owTzWIVynH1eEqnLWMas"

# Admin Info
admin_id = 7556144909
admin_username = "@CryptoRaza0"

# Instamojo Credentials (to be filled after verification)
IM_API_KEY = "<YOUR_INSTAMOJO_API_KEY>"
IM_AUTH_TOKEN = "<YOUR_INSTAMOJO_AUTH_TOKEN>"
WEBHOOK_SECRET = "<RANDOM_WEBHOOK_SECRET>"

# Create Bot Client (used in handlers if needed)
app_bot = Client("CryptoNotifierPro", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

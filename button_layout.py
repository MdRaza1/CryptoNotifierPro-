# button_layout.py

from pyrogram.types import ReplyKeyboardMarkup

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            ["📈 Crypto", "📊 Stock Market"],
            ["🎓 Trading Education"],
            ["🆓 Free Member Features", "🔐 VIP Features"],
            ["👥 Support", "👑 Upgrade VIP"]
        ],
        resize_keyboard=True
    )

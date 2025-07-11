# crypto_news.py
import requests

async def send_crypto_news(client, message):
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"

    try:
        res = requests.get(url).json()
        articles = res['Data'][:3]
        msg = "📰 Top Crypto News:\n\n"
        for a in articles:
            title = a['title']
            link = a['url']
            msg += f"🔹 [{title}]({link})\n"
        await message.reply(msg, disable_web_page_preview=True)
    except:
        await message.reply("❌ Failed to fetch news.")

# crypto_alerts.py
import requests

async def handle_crypto_alerts(client, message):
    try:
        coin = message.text.split(" ", 1)[1].strip().lower()
    except:
        await message.reply("⚠️ Use format: /price BTC")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr,usd"

    try:
        res = requests.get(url).json()
        inr = res[coin]['inr']
        usd = res[coin]['usd']
        await message.reply(f"💰 {coin.upper()} Price:\n🇮🇳 INR: ₹{inr}\n🇺🇸 USD: ${usd}")
    except:
        await message.reply("❌ Coin not found or API error.")

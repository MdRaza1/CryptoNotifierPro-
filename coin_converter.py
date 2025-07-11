# coin_converter.py
import requests

async def convert_coin(client, message):
    try:
        _, coin, amount = message.text.split()
        coin = coin.lower()
        amount = float(amount)
    except:
        await message.reply("⚠️ Use format: /convert BTC 0.5")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr"
    try:
        res = requests.get(url).json()
        usd = res[coin]['usd'] * amount
        inr = res[coin]['inr'] * amount
        await message.reply(f"🔄 {amount} {coin.upper()} is:\n🇮🇳 ₹{round(inr,2)}\n🇺🇸 ${round(usd,2)}")
    except:
        await message.reply("❌ Conversion failed. Check coin name or amount.")

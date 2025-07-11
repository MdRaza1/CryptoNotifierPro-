# crypto_summary.py
import requests

async def crypto_market_summary():
    url = "https://api.coingecko.com/api/v3/global"
    data = requests.get(url).json()["data"]
    msg = (
        f"📊 Market Summary:\n\n"
        f"• Total Market Cap: ${data['total_market_cap']['usd']:.2f}\n"
        f"• BTC Dominance: {data['market_cap_percentage']['btc']:.2f}%\n"
        f"• ETH Dominance: {data['market_cap_percentage']['eth']:.2f}%\n"
        f"• Fear & Greed Index: 🔐 Not available in this API"
    )
    return msg

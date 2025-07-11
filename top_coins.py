# top_coins.py
import requests

async def get_top_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
    res = requests.get(url).json()
    msg = "🏆 Top 5 Cryptocurrencies:\n\n"
    for coin in res:
        msg += f"{coin['market_cap_rank']}. {coin['name']} ({coin['symbol'].upper()})\n"
        msg += f"   💰 ${coin['current_price']} | 📈 {coin['price_change_percentage_24h']}% (24h)\n\n"
    return msg

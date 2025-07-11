# crypto_mover.py
import requests

async def top_gainers_and_losers():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1"
    data = requests.get(url).json()
    sorted_data = sorted(data, key=lambda x: x['price_change_percentage_24h'], reverse=True)

    msg = "📈 Top Gainers (24h):\n"
    for coin in sorted_data[:3]:
        msg += f"{coin['name']} ({coin['symbol'].upper()}): +{coin['price_change_percentage_24h']:.2f}%\n"

    msg += "\n📉 Top Losers (24h):\n"
    for coin in sorted_data[-3:]:
        msg += f"{coin['name']} ({coin['symbol'].upper()}): {coin['price_change_percentage_24h']:.2f}%\n"

    return msg

# crypto_watchlist.py

user_crypto_watchlist = {}

async def add_to_crypto_watchlist(user_id, coin):
    coin = coin.upper()
    if user_id not in user_crypto_watchlist:
        user_crypto_watchlist[user_id] = []
    if coin not in user_crypto_watchlist[user_id]:
        user_crypto_watchlist[user_id].append(coin)
        return f"✅ {coin} added to your crypto watchlist."
    return f"⚠️ {coin} already in your watchlist."

async def view_crypto_watchlist(user_id):
    wl = user_crypto_watchlist.get(user_id, [])
    if not wl:
        return "❌ Your crypto watchlist is empty."
    return "📌 Your Crypto Watchlist:\n" + "\n".join(wl)

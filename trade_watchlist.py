# trade_watchlist.py
user_trade_watchlist = {}

async def add_trade_watchlist(user_id, symbol):
    symbol = symbol.upper()
    if user_id not in user_trade_watchlist:
        user_trade_watchlist[user_id] = []
    if symbol not in user_trade_watchlist[user_id]:
        user_trade_watchlist[user_id].append(symbol)
        return f"✅ {symbol} added to your trade watchlist."
    return f"⚠️ {symbol} already in your watchlist."

async def view_trade_watchlist(user_id):
    wl = user_trade_watchlist.get(user_id, [])
    if not wl:
        return "❌ Your trade watchlist is empty."
    return "📌 Your Trade Watchlist:\n" + "\n".join(wl)

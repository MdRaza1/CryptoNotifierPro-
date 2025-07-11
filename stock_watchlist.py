# stock_watchlist.py

user_watchlists = {}

async def update_stock_watchlist(user_id, stock):
    stock = stock.upper()
    if user_id not in user_watchlists:
        user_watchlists[user_id] = []
    if stock not in user_watchlists[user_id]:
        user_watchlists[user_id].append(stock)
        return f"✅ {stock} added to your watchlist."
    else:
        return f"⚠️ {stock} already exists in your watchlist."

async def view_watchlist(user_id):
    watchlist = user_watchlists.get(user_id, [])
    if not watchlist:
        return "❌ Your watchlist is empty."
    return "📌 Your Stock Watchlist:\n" + "\n".join([f"• {s}" for s in watchlist])

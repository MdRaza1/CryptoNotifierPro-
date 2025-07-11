# portfolio_alert.py

user_portfolios = {}

async def update_portfolio(user_id, coin, amount):
    if user_id not in user_portfolios:
        user_portfolios[user_id] = {}
    user_portfolios[user_id][coin] = amount
    return f"✅ {amount} {coin.upper()} added to your portfolio."

async def get_portfolio(user_id):
    return user_portfolios.get(user_id, {})

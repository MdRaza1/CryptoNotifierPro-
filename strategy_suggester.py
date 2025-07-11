# strategy_suggester.py
async def suggest_strategy(market_condition):
    if market_condition.lower() == "bullish":
        return "📈 Strategy: Trend-following (e.g. Moving Average Cross)"
    elif market_condition.lower() == "bearish":
        return "📉 Strategy: Pullback shorting or breakdown plays"
    else:
        return "⚠️ Market unclear. Use range-bound strategy like VWAP."

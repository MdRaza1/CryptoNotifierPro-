# trailing_sl_calc.py
def get_trailing_sl(entry, current, trail_percent):
    tsl = current - (current * trail_percent / 100)
    return f"🔁 Trailing SL should be set at: ₹{tsl:.2f}"

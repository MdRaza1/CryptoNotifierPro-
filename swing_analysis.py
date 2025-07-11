# swing_analysis.py

def calculate_swing_zones(price):
    support = price * 0.97
    resistance = price * 1.03
    return f"""🌀 Swing Trade Zones:

🔽 Support: ₹{support:.2f}
🔼 Resistance: ₹{resistance:.2f}"""

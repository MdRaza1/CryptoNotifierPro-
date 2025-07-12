def calculate_lot_size(capital, risk_percent, stop_loss):
    risk_amount = capital * (risk_percent / 100)
    lot_size = risk_amount / stop_loss
    return f"📊 Lot Size: {int(lot_size)} units (Risk ₹{risk_amount:.2f})"
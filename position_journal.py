# position_journal.py
journal = []

def log_trade(entry, exit, pnl):
    journal.append({"entry": entry, "exit": exit, "pnl": pnl})

def get_journal():
    if not journal:
        return "📝 No trades logged yet."
    return "\n".join([f"{j['entry']} ➜ {j['exit']} | PnL: ₹{j['pnl']}" for j in journal])

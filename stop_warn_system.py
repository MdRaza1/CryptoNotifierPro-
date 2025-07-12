# stop_warn_system.py
loss_streak = 0

def record_loss():
    global loss_streak
    loss_streak += 1
    if loss_streak >= 3:
        return "🛑 3 Losses in a row. STOP trading and review your strategy."
    return f"⚠️ Loss count: {loss_streak}"

def reset_streak():
    global loss_streak
    loss_streak = 0

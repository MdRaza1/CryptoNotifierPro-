# risk_analyzer.py
def analyze_risk(capital, exposure):
    if exposure > capital:
        return "❌ Overexposed! Reduce your trade size."
    elif exposure < capital * 0.5:
        return "⚠️ Under-utilizing capital. Consider optimizing lot size."
    else:
        return "✅ Risk level is balanced."

# auto_sector_tracker.py

import random

async def hot_sectors_today():
    sectors = ["IT", "Pharma", "Auto", "FMCG", "Infra", "Banking", "Energy"]
    hot = random.sample(sectors, 2)
    cold = random.sample([s for s in sectors if s not in hot], 2)

    return f"""🔥 Hot Sectors: {', '.join(hot)}
❄️ Cold Sectors: {', '.join(cold)}"""

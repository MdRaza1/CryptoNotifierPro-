# stock_prediction.py
import random

async def handle_stock_prediction(client, message):
    try:
        stock = message.text.split(" ", 1)[1].strip().upper()
    except:
        await message.reply("⚠️ Use format: /predict TATAMOTORS")
        return

    trend = random.choice(["📈 Likely to go UP", "📉 May go DOWN", "⚖️ Sideways movement expected"])
    await message.reply(f"📊 Prediction for {stock}:\n{trend}\n\n(Disclaimer: AI-based hint, not financial advice)")

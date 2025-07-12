# quiz_module.py

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import json
import random

# Load quiz data
def load_quiz():
    with open("quiz_data.json", "r") as f:
        return json.load(f)

@Client.on_message(filters.command("quiz"))
async def quiz_command(client: Client, message: Message):
    quiz_data = load_quiz()
    question_data = random.choice(quiz_data)

    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["answer"]

    # Store correct answer in callback_data
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=opt, callback_data=f"quiz|{opt}|{correct_answer}")]
        for opt in options
    ])

    await message.reply(f"🧠 Quiz Time!\n\n❓ {question}", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^quiz"))
async def quiz_answer(client: Client, callback_query: CallbackQuery):
    _, selected, correct = callback_query.data.split("|")

    if selected == correct:
        await callback_query.answer("✅ Correct!", show_alert=True)
    else:
        await callback_query.answer(f"❌ Incorrect! Correct: {correct}", show_alert=True)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_yes_no_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Да"), KeyboardButton("Нет"))
    return keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
    KeyboardButton(
        text='Записаться на мероприятие'
    )
    ]
], resixe_keyboard=True, one_time_keyboard=True, input_field_placeholder="Для продолжения нажмите на кнопку ниже")

get_yes_no_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='да'),
        KeyboardButton(text='нет'),
    ]
], resixe_keyboard=True, one_time_keyboard=True)



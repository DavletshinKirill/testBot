from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard_token = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ввести TOKEN")
    ]
], one_time_keyboard=True)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ввести команду")
    ],
    [
        KeyboardButton(text="Ввести результат")
    ]
], one_time_keyboard=True)

binary_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Да")
    ],
    [
        KeyboardButton(text="Нет")
    ]
]
)

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Предметы"),
            KeyboardButton(text="Квесты")
        ]
    ], resize_keyboard=True
)


item_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Категория 1"),
            KeyboardButton(text="Категория 2")
        ],
        [
          KeyboardButton(text="Вернуться")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите категорию"

)
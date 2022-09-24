from typing import Optional

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_default_keyboard(keys: Optional[str] | Optional[list[str]], one_time_keyboard=None, **kwargs) -> ReplyKeyboardMarkup:
    if keys is None:
        raise TypeError('Key must be str or list[str]')

    keyboard = []
    if isinstance(keys, str):
        keyboard.append([KeyboardButton(text=keys)])
    elif isinstance(keys, list):
        for key in keys:
            keyboard.append([KeyboardButton(text=key)])

    keyboard_markup = ReplyKeyboardMarkup(keyboard=keyboard,
                                          resize_keyboard=True,
                                          one_time_keyboard=one_time_keyboard,
                                          **kwargs)
    return keyboard_markup

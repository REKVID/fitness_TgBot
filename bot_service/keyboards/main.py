"""Модуль с основными клавиатурами для бота.

Содержит пример inline-клавиатуры.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard() -> InlineKeyboardMarkup:
    """Возвращает основную inline-клавиатуру.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой "Начать".
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Начать", callback_data="start")]]
    )
    return keyboard

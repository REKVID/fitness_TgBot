"""Модуль с Router'ом для команды /start.

Содержит обработчик приветствия пользователя.
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    """Обрабатывает команду /start.

    Args:
        message (Message): Входящее сообщение от пользователя.
    """
    await message.answer("Добро пожаловать в фитнес-бот!")

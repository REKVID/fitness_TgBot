"""Модуль с FSM-состояниями пользователя.

Содержит пример состояния для регистрации.
"""

from aiogram.fsm.state import StatesGroup, State


class RegistrationState(StatesGroup):
    """Состояния для процесса регистрации пользователя."""

    waiting_for_name = State()
    waiting_for_age = State()

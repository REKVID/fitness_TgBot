"""Pydantic-модель для пользователя (DTO).

Используется для обмена данными между сервисами.
"""

from pydantic import BaseModel


class UserDTO(BaseModel):
    """DTO для пользователя."""

    telegram_id: int
    gender: str
    birth_date: str
    subscription_type: str
    current_workout_program: str
    training_goal: str
    training_place: str

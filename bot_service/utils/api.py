"""Модуль для взаимодействия с user_service через прямые Python-вызовы.

Содержит пример синхронного клиента.
"""

from user_service.user_db_manager import get_user, add_user, delete_user
from models.user import UserDTO


class UserServiceAPI:
    """Клиент для user_service через прямые вызовы функций."""

    @staticmethod
    def get_user(telegram_id: int) -> UserDTO:
        """Получает пользователя по telegram_id.

        Args:
            telegram_id (int): Telegram ID пользователя.
        Returns:
            UserDTO: Данные пользователя.
        """
        user_data = get_user(telegram_id)
        if isinstance(user_data, dict):
            return UserDTO(**user_data)
        raise ValueError(user_data)

    @staticmethod
    def add_user(user: UserDTO) -> str:
        """Добавляет пользователя.

        Args:
            user (UserDTO): Данные пользователя.
        Returns:
            str: Результат добавления.
        """
        return add_user(
            user.telegram_id,
            user.gender,
            user.birth_date,
            user.subscription_type,
            user.current_workout_program,
            user.training_goal,
            user.training_place,
        )

    @staticmethod
    def delete_user(telegram_id: int) -> str:
        """Удаляет пользователя по telegram_id.

        Args:
            telegram_id (int): Telegram ID пользователя.
        Returns:
            str: Результат удаления.
        """
        return delete_user(telegram_id)

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "users.db")


def migrate_db():
    """Добавляет новые поля training_goal и training_place в таблицу users, если их нет."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Проверяем наличие столбцов
    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    if "training_goal" not in columns:
        cursor.execute(
            "ALTER TABLE users ADD COLUMN training_goal TEXT NOT NULL DEFAULT ''"
        )
    if "training_place" not in columns:
        cursor.execute(
            "ALTER TABLE users ADD COLUMN training_place TEXT NOT NULL DEFAULT ''"
        )
    conn.commit()
    conn.close()


def init_db():
    """Инициализация базы данных и таблицы пользователей.

    Создаёт таблицу users, если она ещё не существует. Если таблица уже есть, вызывает миграцию.

    Args:
        Нет.

    Returns:
        Нет.

    Пример:
        >>> init_db()
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            gender TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            subscription_type TEXT NOT NULL,
            current_workout_program TEXT NOT NULL,
            training_goal TEXT NOT NULL,
            training_place TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    migrate_db()


def add_user(
    telegram_id,
    gender,
    birth_date,
    subscription_type,
    current_workout_program,
    training_goal,
    training_place,
):
    """Добавляет нового пользователя в базу данных.

    Args:
        telegram_id (int): Telegram ID пользователя (уникальный идентификатор).
        gender (str): Пол пользователя ('male' или 'female').
        birth_date (str): Дата рождения пользователя в формате 'YYYY-MM-DD'.
        subscription_type (str): Тип подписки пользователя.
        current_workout_program (str): Текущий вариант программы тренировок.
        training_goal (str): Цель тренировок пользователя.
        training_place (str): Место занятий (дом, улица, тренажерный зал).

    Returns:
        str: Сообщение об успешном добавлении или ошибке.

    Пример:
        >>> add_user(123456789, 'male', '1990-01-01', 'premium', 'program_1', 'похудение', 'дом')
        'Пользователь успешно добавлен.'
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (telegram_id, gender, birth_date, subscription_type, current_workout_program, training_goal, training_place)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                telegram_id,
                gender,
                birth_date,
                subscription_type,
                current_workout_program,
                training_goal,
                training_place,
            ),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return f"Ошибка: пользователь с telegram_id {telegram_id} уже существует."
    except Exception as e:
        return f"Ошибка при добавлении пользователя: {e}"
    finally:
        conn.close()
    return "Пользователь успешно добавлен."


def get_user(telegram_id):
    """Извлекает информацию о пользователе по telegram_id.

    Args:
        telegram_id (int): Telegram ID пользователя.

    Returns:
        dict | str: Словарь с данными пользователя или сообщение об ошибке.

    Пример:
        >>> get_user(123456789)
        {'telegram_id': 123456789, 'gender': 'male', ...}
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        user = cursor.fetchone()
        if user is None:
            return f"Пользователь с telegram_id {telegram_id} не найден."
        return {
            "telegram_id": user[0],
            "gender": user[1],
            "birth_date": user[2],
            "subscription_type": user[3],
            "current_workout_program": user[4],
            "training_goal": user[5],
            "training_place": user[6],
        }
    except Exception as e:
        return f"Ошибка при получении пользователя: {e}"
    finally:
        conn.close()


def delete_user(telegram_id):
    """Удаляет пользователя из базы данных по telegram_id.

    Args:
        telegram_id (int): Telegram ID пользователя.

    Returns:
        str: Сообщение об успешном удалении или ошибке.

    Пример:
        >>> delete_user(123456789)
        'Пользователь с telegram_id 123456789 успешно удалён.'
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE telegram_id = ?", (telegram_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return f"Пользователь с telegram_id {telegram_id} не найден."
        return f"Пользователь с telegram_id {telegram_id} успешно удалён."
    except Exception as e:
        return f"Ошибка при удалении пользователя: {e}"
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    # Примеры использования:
    # print(add_user(123456789, 'male', '1990-01-01', 'premium', 'program_1', 'похудение', 'дом'))
    # print(get_user(123456789))
    # print(delete_user(123456789))

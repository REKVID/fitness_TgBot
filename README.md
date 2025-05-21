# Fitness Telegram Bot

Telegram-бот для тренировок и фитнеса с микросервисной архитектурой.

## Структура проекта

```
/
├── gateway/               # API gateway
├── bot_service/           # Telegram Bot сервис
├── workout_service/       # Сервис тренировок
├── payment_service/       # Платежный сервис
├── openai_service/        # Интеграция с OpenAI
├── user_service/          # Сервис пользователей
├── media_storage/         # Хранилище медиа-файлов
│   ├── exercises.db       # База данных упражнений
│   ├── mediaMan/          # Медиа-файлы упражнений для мужчин
│   └── mediaWomen/        # Медиа-файлы упражнений для женщин
├── shared/                # Общие компоненты и утилиты
└── .env                   # Переменные окружения
```

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/REKVID/fitness_TgBot.git
cd fitness_TgBot
```

2. Создайте и настройте файл .env:
```bash
cp .env.example .env
# Отредактируйте .env файл, добавив необходимые параметры
```

3. Запустите проект (инструкции будут добавлены позже)

## Лицензия

[MIT](LICENSE)

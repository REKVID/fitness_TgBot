"""Точка входа для Telegram-бота на aiogram v3.

Подключает все Router'ы и запускает бота.
"""

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# from handlers import start_router  # Пример импорта


async def main():
    # TODO: Заменить на чтение токена из .env
    bot = Bot(token="BOT_TOKEN")
    dp = Dispatcher(storage=MemoryStorage())
    # dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

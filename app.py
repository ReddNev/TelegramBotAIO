import logging
from aiogram import executor
from create_bot import dp
from handlers import user

logging.basicConfig(level=logging.INFO)

""" Function launch """
user.register_handlers_client(dp)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
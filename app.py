import logging
from aiogram import executor
from create_bot import dp, bot
from handlers import user
from aiogram.types import BotCommand

logging.basicConfig(level=logging.INFO)


async def set_commands(bot: bot):
    commands = [
        BotCommand(command="/start", description="Запуск бота и регистрация новых пользователей"),
        BotCommand(command="/wallets", description="Ваш кошелек"),

    ]
    await bot.set_my_commands(commands)


""" Function launch """
user.register_handlers_client(dp)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

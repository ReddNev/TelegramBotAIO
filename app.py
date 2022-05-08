import logging

from aiogram import executor
from aiogram.types import BotCommand

from create_bot import dp, bot
from handlers import user

logging.basicConfig(level=logging.INFO)


async def set_commands(bot: bot):
    commands = [
        BotCommand(command="/start", description="Запуск бота и регистрация новых пользователей"),
        BotCommand(command="/wallets", description="Ваш кошелек"),

    ]
    await bot.set_my_commands(commands)


"""Launch handlers"""
user.register_handlers_client(dp)


if __name__ == "__main__":
    # Bot launch
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as cnf

storage = MemoryStorage()
bot = Bot(cnf.TOKEN)
dp = Dispatcher(bot, storage=storage)

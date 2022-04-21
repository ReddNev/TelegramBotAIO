import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config as cnf
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(cnf.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def start_or_help(message: types.Message):
    ''' Response to command /help and /start '''

    text = 'Hi, i am a bot helper'

    await message.answer(text)


@dp.message_handler(commands=['button'])
async def button(message):
    start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton(text='How can I help')
    btn2 = types.InlineKeyboardButton(text='Bye')
    start_markup.add(btn1, btn2)
    await message.answer('Hello', reply_markup=start_markup)


@dp.message_handler(lambda message: message.text == 'How can I help')
async def with_puree(message: types.Message):
    await message.answer('I can do...')


@dp.message_handler(lambda message: message.text == 'Bye')
async def without_puree(message: types.Message):
    await message.answer('Bye, Bye')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
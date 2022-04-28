import logging
from aiogram import Bot, Dispatcher, executor, types
import config as cnf
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.database import get_user_by_id, insert_new_user


storage = MemoryStorage()
bot = Bot(cnf.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ''' Response to command start '''
    chat_id = message.from_user.id
    username = message.from_user.username
    user_info = get_user_by_id(_id=chat_id)
    if user_info:
        await message.answer("Bot is ready to go")
    else:
        insert_new_user(chat_id=chat_id, username=username)
        await message.answer("User added to the system")


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
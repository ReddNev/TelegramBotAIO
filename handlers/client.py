from aiogram import types, Dispatcher
from database.database import get_user_by_id, insert_new_user
from keyboards import markups
from create_bot import dp, bot


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ''' Response to command start '''
    chat_id = message.from_user.id
    username = message.from_user.username
    user_info = get_user_by_id(_id=chat_id)
    if user_info:
        await message.answer("Bot is ready to go", reply_markup=markups.main_menu)
    else:
        insert_new_user(chat_id=chat_id, username=username)
        await message.answer("User added to the system")


# @dp.message_handler()
async def client_info(message: types.Message):
    if message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'Информация', reply_markup=markups.info_menu)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markups.main_menu)
    elif message.text == 'Кошелек':
        await bot.send_message(message.from_user.id, 'Кошелке', reply_markup=markups.purse_menu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(client_info)


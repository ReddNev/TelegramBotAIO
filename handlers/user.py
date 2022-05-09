import typing

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import bot
from database.database import get_user_by_id, insert_new_user, get_addres_by_id

from services.client import Client
from config import WALLETS, WALLETS_COMMAND, logger


async def start(message: types.Message):
    """Response to command start"""
    chat_id = message.from_user.id
    username = message.from_user.username
    user_info = get_user_by_id(_id=chat_id)
    if user_info:
        await message.answer("Bot is ready to go")
    else:
        insert_new_user(chat_id=chat_id, username=username)
        await message.answer("User added to the system")


async def get_wallets(message: typing.Union[types.CallbackQuery, types.Message]):
    logger.info("get_wallets command")

    """
    Возвращает кошельки
    :param :
    :return:
    """
    group_btn_s = InlineKeyboardMarkup(row_width=2)
    btn_s = []
    for wallet_key in WALLETS.keys():
        btn_s.append(
            InlineKeyboardButton(f"Wallet {wallet_key.title()}", callback_data=f"wallet_{wallet_key.lower()}")
        )
        # callback_data TYPE: wallet_tron
    group_btn_s.add(*btn_s)
    if isinstance(message, types.CallbackQuery):
        # types.CallbackQuery
        await message.message.edit_text('Ваши кошельки', reply_markup=group_btn_s)
    elif isinstance(message, types.Message):
        # types.Message
        await message.answer("Ваш кошельки", reply_markup=group_btn_s)


async def get_wallet_commands(callback_query: types.CallbackQuery):
    logger.info("get_wallet_commands command")

    group_btn_s = InlineKeyboardMarkup(row_width=2)
    btn_s = []
    for method_key, method_value in WALLETS_COMMAND.items():
        btn_s.append(
            InlineKeyboardButton(f"{method_value}", callback_data=f"type_{method_key.lower()}_{callback_query.data[7:]}"
                                 )
        )
        # callback_query.data[7:] TYPE: NETWORK --- TRON, SOLANA и тд
        # method_key TYPE: METHOD --- BALANCE, SEND и тд
        # callback_data TYPE: type_<METHOD>_<NETWORK>
    back = InlineKeyboardButton('Back', callback_data='wallets')
    btn_s.append(back)
    group_btn_s.add(*btn_s)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text='Что Вы хотите:', reply_markup=group_btn_s)


async def get_tokens(callback_query: types.CallbackQuery = None):
    logger.info("get_tokens command")

    group_btn_s = InlineKeyboardMarkup(row_width=2)
    btn_s = []
    for wallet_token in WALLETS.get(callback_query.data[13:]):
        btn_s.append(
            InlineKeyboardButton(f"{callback_query.data[13:].title()} - {wallet_token.upper()}",
                                 callback_data=f"balance_{callback_query.data[13:].lower()}_{wallet_token.lower()}")
        )
    # callback_query.data[13:] TYPE: NETWORK --- TRON, SOLANA и тд
    # wallet_token TYPE: TOKEN --- TRX, USDT и тд
    # callback_data TYPE: balance_<NETWORK>_<TOKEN>
    back = InlineKeyboardButton('Back', callback_data=f'wallet_{callback_query.data[13:]}')
    btn_s.append(back)
    group_btn_s.add(*btn_s)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text='Какой ТОКЕН:', reply_markup=group_btn_s)


async def get_balance(callback_query: types.CallbackQuery):
    logger.info("get_balance command")

    _, network, token = is_valid(data=callback_query.data)
    balance: typing.Dict = await Client.get_balance(
        network=network,
        token=token,
        # Create table 'wallet_model'
        address=get_addres_by_id(callback_query.message.from_user.id)
    )
    await callback_query.answer(
        f"Ваш баланс: {balance.get('balance')} {network.upper()} {token.upper()}",
        True
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

    dp.register_message_handler(get_wallets, commands=['wallets'])
    dp.register_callback_query_handler(get_wallets, lambda x: x.data == 'wallets')

    dp.register_callback_query_handler(get_wallet_commands, lambda x: x.data[:7] == 'wallet_' and x.data[7:] in WALLETS)
    dp.register_callback_query_handler(get_tokens, lambda x: x.data[:13] == 'type_balance_' and x.data[13:] in WALLETS)
    dp.register_callback_query_handler(get_balance, lambda x: x.data[:8] == "balance_")


def is_valid(data: str) -> typing.Union[typing.Tuple, bool]:
    """
    :param data: <METHOD>_<NETWORK>_<TOKEN>
    """
    method, network, token = tuple(data.split("_"))
    if method not in list(WALLETS_COMMAND.keys()):
        return False
    if network not in list(WALLETS.keys()):
        return False
    for tok in WALLETS.get(network):
        if tok == token:
            return method, network, token
    else:
        return False


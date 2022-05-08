import os
import decimal
import logging
from dotenv import load_dotenv

decimals = decimal.Context()
decimals.prec = 8

logger = logging.getLogger(__name__)

load_dotenv()

TOKEN = os.getenv('TOKEN')
NAME = 'MyMoneyBot'

DATABASE_PATH = os.getenv('DATABASE_PATH')

WALLETS = {
    # NETWORK: [TOKEN, ...]
    "tron": [
        'trx',
        'usdt'
    ],
    "solana": [
        "sol",
        "usdt"
    ]
}

WALLETS_COMMAND = {
    'balance': "Get Balance",
    'send': 'Send',
    'receive': 'Receive'
}
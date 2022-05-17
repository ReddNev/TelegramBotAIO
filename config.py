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


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(ROOT_DIR, 'files')
if "files" not in os.listdir(ROOT_DIR):
    os.mkdir(BASE_DIR)
QR_CODE_PATH = os.path.join(BASE_DIR, 'qr_code_address.png')

DOMAINS = {
    'TRON': os.getenv('TRON_DOMAIN')
}

from config import decimals
import random


class Client:

    @staticmethod
    async def get_balance(network: str, token: str, address: str):
        return {
            "balance": decimals.create_decimal(random.randint(124, 155)),
            "token": token
        }
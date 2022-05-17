from typing import List, Dict, Optional
import aiohttp

from config import logger


async def get_balance_api(domain: str, network: str, token: str, address: str):
    try:
        url = f'https://{domain}/api/balance/{network}/{token}/{address}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                if not response.ok:
                    logger.error(f'GET MESSAGE WAS NOT SENT.')
                else:
                    logger.error(f'GET MESSAGE HAS BEEN SENT.')
                return await response.json()

    except Exception as error:
        raise error


async def create_transaction(chat_id: int, network: str, domain: str, outputs: List[Dict],
                             inputs: Optional[List[str]] = None):
    try:
        url = f'https://{domain}/api/create/transaction'
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json={
                'chatID': chat_id,
                'network': network,
                'inputs': inputs,
                'outputs': outputs
            }) as response:
                if not response.ok:
                    logger.error(f'POST MESSAGE WAS NOT SENT.')
                else:
                    logger.error(f'POST MESSAGE HAS BEEN SENT.')
                return await response.json()

    except Exception as error:
        raise error


async def send_transaction(chat_id: int, network: str, domain: str,
                           outputs: List[Dict], inputs: Optional[List[str]] = None):
    try:
        url = f'https://{domain}/api/send'
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json={
                'chatID': chat_id,
                'network': network,
                'inputs': inputs,
                'outputs': outputs
            }) as response:
                if not response.ok:
                    logger.error(f'POST MESSAGE WAS NOT SENT. {await response.json()}')
                else:
                    logger.error(f'POST MESSAGE HAS BEEN SENT.')

    except Exception as error:
        raise error


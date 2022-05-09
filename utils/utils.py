import pyqrcode as pq
from config import QR_CODE_PATH
import aiofiles


async def get_qr_code(address: str):
    """
    Generate qr code by address
    :param address: crypto wallet address
    :return:
    """
    qr_code = pq.create(address)
    qr_code.png(QR_CODE_PATH, scale=6)

    async with aiofiles.open(QR_CODE_PATH, 'rb') as file:
        code = await file.read()
    return code


async def delete_qr_code():
    pass

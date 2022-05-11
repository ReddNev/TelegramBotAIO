import pyqrcode as pq
import os
import aiofiles
from config import QR_CODE_PATH


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
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), QR_CODE_PATH)
        os.remove(path)
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")





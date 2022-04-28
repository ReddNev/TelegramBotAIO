import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
NAME = 'MyMoneyBot'

DATABASE_PATH = os.getenv('DATABASE_PATH')

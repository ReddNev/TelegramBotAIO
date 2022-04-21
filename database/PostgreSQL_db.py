import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
except Exception as _ex:
    print('[INFO] Error while working PostgeSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgeSQL connection closed')

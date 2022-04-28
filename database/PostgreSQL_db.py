import psycopg2.extras
from config import DATABASE_PATH


con = None
try:
    con = psycopg2.connect(DATABASE_PATH)
    with con.cursor() as cur:
        cur.execute('SELECT version()')
        print(f'SERVER version: {cur.fetchone()}')

    with con.cursor() as cur:
        cur.execute(
            """CREATE TABLE IF NOT EXISTS users(
            id integer PRIMARY KEY,
            username varchar(20) NOT NULL,
            is_admin boolean NOT NULL DEFAULT false);"""
        )
except Exception as _ex:
    raise _ex
finally:
    con.commit()


import psycopg2
import config as cnf


def get_user_by_id(_id: int):
    sql = f"SELECT chat_id FROM users WHERE chat_id = {_id}"
    con = psycopg2.connect(cnf.DATABASE_PATH)
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchone()


def insert_new_user(chat_id, username):
    sql = f"INSERT INTO users(username, chat_id) VALUES(%s, %s)", (chat_id, username)
    con = psycopg2.connect(cnf.DATABASE_PATH)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return True

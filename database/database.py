import psycopg2
import config as cnf


def get_user_by_id(_id: int):
    sql = f"SELECT id FROM users WHERE id = {_id}"
    con = psycopg2.connect(cnf.DATABASE_PATH)
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchone()


def insert_new_user(chat_id, username):
    sql = f"INSERT INTO users(username, id) VALUES('%s', %i)" % (f"@{username}", chat_id)
    con = psycopg2.connect(cnf.DATABASE_PATH)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return True


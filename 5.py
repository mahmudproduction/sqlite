import sqlite3

conn = sqlite3.connect(r'/home/owner/py/sqlite/telebot.db')
cur = conn.cursor()
cur.execute("DELETE FROM users;")
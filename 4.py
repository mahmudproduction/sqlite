import sqlite3 #загрузки библиотеки
conn = sqlite3.connect(r'/home/owner/py/sqlite/telebot.db')
cur = conn.cursor()#После создания объекта соединения с базой данных нужно создать объект cursor

# cur.execute("SELECT * FROM users;")
# all_results = cur.fetchall()
# for row in all_results:
# 	print(row[1])

cur.execute("SELECT name FROM users WHERE name REGEXP 'Plaudis';")
one_result = cur.fetchone()
print(f"{one_result }\n")
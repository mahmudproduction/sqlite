import sqlite3 #загрузки библиотеки
conn = sqlite3.connect(r'/home/owner/py/sqlite/orders.db') #За соединение будет отвечать переменная conn. Если файл уже существует, то функция connect осуществит подключение к нему.перед строкой с путем стоит символ «r». Это дает понять Python, что речь идет о «сырой» строке, где символы «/» не отвечают за экранирование.
#conn = sqlite3.connect(:memory:) Eще один способ создания баз данных с помощью SQLite в Python — создание их в памяти. 
cur = conn.cursor()#После создания объекта соединения с базой данных нужно создать объект cursor
#Теперь выполнять запросы можно следующим образом:
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY  ,
   fname TEXT,
   lname TEXT,
   gender TEXT);
   """)
        cur.execute("""CREATE TABLE IF NOT EXISTS chats ( id INTEGER NOT NULL, chat_title TEXT, chat_u_name TEXT, chat_id INTEGER, u_id INTEGER, u_mes_id INTEGER, msg TEXT, n_time INTEGER,  )""")

#Обратите внимание на то, что сами запросы должны быть помещены в кавычки — это важно. Это могут быть одинарные, двойные или тройные кавычки. Последние используются в случае особенно длинных запросов, которые часто пишутся на нескольких строках.
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
   """)
 ''' cur.execute("""CREATE TABLE IF NOT EXISTS test_users(
        id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
        u_id   TEXT ,
        f_name   TEXT,
        l_name  TEXT,
        u_name  TEXT,
        chat TEXT,
        chat_title INTEGER,
        add_time TEXT,
        auth   INTEGER);""")'''
   
#По аналогии с запросом для создания таблиц для добавления данных также нужно использовать объект cursor.
cur.execute("""INSERT INTO users(userid, fname, lname, gender)  VALUES('1', 'Alex', 'Smith', 'male');""") 
 
#В Python часто приходится иметь дело с переменными, в которых хранятся значения. Например, это может быть кортеж с информацией о пользователе.
user = ('5', 'Lois', 'ARMSTRONG', 'GOOD MAN')
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
#можно добавить несколько пользователей:
more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
#Но нужно использовать функцию executemany вместо обычной execute:
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)

conn.commit() #Сохраняем изменения с помощью функции commit для объекта соединения.
#----------------------------------------->Получение данных с SQLite в Python
#Начнем с использования функции fetchone(). Создадим переменную one_result для получения только одного результата:
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone() #Возвращает кортеж
print(f"{one_result}\n")
#Если же нужно получить много данных, то используется функция fetchmany(). Выполним другой скрипт для генерации 3 результатов:
cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(f"{three_results}\n")
#Функцию fetchall() можно использовать для получения всех результатов.  
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall() # возвращает список кортежей
print(all_results)
#Функцию fetchall() можно использовать для получения всех результатов включение цикла.
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
for row in all_results:
   print (row[1])

#Теперь рассмотрим процесс удаления данных с SQLite в Python. Здесь та же структура. Предположим, нужно удалить любого пользователя с фамилией «Parker». Напишем следующее:
# cur.execute("DELETE FROM users WHERE lname='Parker';")
# conn.commit()
#WHERE f_name  LIKE '%"+str(avv)+"%'   Поиск
#Если затем сделать следующей запрос Будет выведен пустой список, подтверждающий, что запись удалена.

cur.execute("select * from users where lname='Parker'")
print(cur.fetchall())
#Наконец, посмотрим, как использовать объединение данных для более сложных запросов. Предположим, нужно сгенерировать запрос, включающий имя и фамилию каждого покупателя заказа.Для этого напишем следующее:
cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;""")
#Просмотреть количество записей в базе:
SELECT COUNT(*) FROM t1;
SELECT albumid,   COUNT(*) FROM tracks GROUP BY albumid HAVING COUNT(*) > 25;
print(cur.fetchall())
print ("<a href = >")
UPDATE table1 SET d = 55 WHERE a = 1  #Добавить в уже имеющийся строки


# PHP 
# https://www.tutorialspoint.com/sqlite/sqlite_php.htm

 
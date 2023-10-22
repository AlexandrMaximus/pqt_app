import sqlite3

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('D:/tkinter_app/my_database.db')
c = conn.cursor()

# Выполните запрос SELECT к вашей таблице
c.execute('SELECT * FROM операции')

# Получите все строки из результата запроса
rows = c.fetchall()

# Выведите каждую строку
for row in rows:
    print(row)

import sqlite3

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('my_database.db')

# Создайте курсор для выполнения SQL-запросов
c = conn.cursor()

# Создайте таблицу
c.execute('''
    CREATE TABLE my_table
    (участок TEXT, фамилия TEXT, шифр_детали TEXT, наименование_детали TEXT,
    количество_деталей INTEGER, операция TEXT, норма_времени_на_единицу REAL)
''')

# Вставьте данные в таблицу
c.execute('''
    INSERT INTO my_table VALUES 
    ('участок1', 'фамилия1', 'шифр1', 'деталь1', 10, 'операция1', 0.5)
''')

# Сохраните изменения
conn.commit()

# Закройте соединение с базой данных
conn.close()
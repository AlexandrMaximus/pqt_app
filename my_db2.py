import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('my_db2.db')

# Создаем курсор
c = conn.cursor()

# Создаем таблицы
c.execute('''
    CREATE TABLE IF NOT EXISTS участки (
        id INTEGER PRIMARY KEY,
        участок TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS разряды (
        id INTEGER PRIMARY KEY,
        разряд TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS работники (
        id INTEGER PRIMARY KEY,
        имя TEXT,
        разряд TEXT,
        FOREIGN KEY (разряд) REFERENCES разряды (id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS детали (
        id INTEGER PRIMARY KEY,
        шифр_детали TEXT,
        наименование_детали TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS инструкции (
        id INTEGER PRIMARY KEY,
        номер_инструкции TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS статус (
        id INTEGER PRIMARY KEY,
        статус TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS смены (
        id INTEGER PRIMARY KEY,
        смена TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS операции (
        id INTEGER PRIMARY KEY,
        шифр_детали TEXT,
        наименование_детали TEXT,
        операция TEXT,
        трудозатраты REAL,
        FOREIGN KEY (шифр_детали) REFERENCES детали (id),
        FOREIGN KEY (наименование_детали) REFERENCES детали (id)
    )
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
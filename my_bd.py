from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QCompleter
from PyQt5.QtCore import Qt
import sqlite3

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('D:/pqt_app/my_database.db')
c = conn.cursor()

# Создайте таблицы, если они еще не существуют
c.execute('CREATE TABLE IF NOT EXISTS участки (id INTEGER PRIMARY KEY, участок TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS работники (id INTEGER PRIMARY KEY, фамилия TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS детали (id INTEGER PRIMARY KEY, шифр_детали TEXT, наименование_детали TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS операции (id INTEGER PRIMARY KEY, участок TEXT, фамилия TEXT, шифр_детали TEXT, наименование_детали TEXT, операция TEXT, норма_времени_на_единицу REAL)')
c.execute('CREATE TABLE IF NOT EXISTS инструкции (id INTEGER PRIMARY KEY, номер_ТБ_инструкции TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS статус (id INTEGER PRIMARY KEY, статус TEXT)')


# Создайте приложение PyQt
app = QApplication([])

# Создайте главное окно
window = QWidget()
layout = QVBoxLayout(window)

# Создайте поля для ввода данных
fields = ['участок', 'фамилия', 'шифр_детали', 'наименование_детали', 'операция', 'норма_времени_на_единицу']
entries = {}

for field in fields:
    # Создайте поле для ввода для каждого поля
    label = QLabel(field)
    layout.addWidget(label)
    entry = QLineEdit()
    c.execute(f'SELECT DISTINCT {field} FROM операции')
    data = c.fetchall()
    completer = QCompleter([str(row[0]) for row in data])
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    entry.setCompleter(completer)
    layout.addWidget(entry)
    entries[field] = entry

# Создайте функцию для сохранения данных
def save_data():
    try:
        # Сохраните данные в базу данных
        c.execute(f'''
            INSERT INTO операции (участок, фамилия, шифр_детали, наименование_детали, операция, норма_времени_на_единицу) VALUES 
            ('{entries["участок"].text()}', '{entries["фамилия"].text()}', '{entries["шифр_детали"].text()}', '{entries["наименование_детали"].text()}', '{entries["операция"].text()}', {entries["норма_времени_на_единицу"].text()})
        ''')
        conn.commit()
        # Показать сообщение об успешном сохранении
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Данные успешно сохранены!")
        msgBox.exec_()
    except Exception as e:
        # Показать сообщение об ошибке
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(f"Произошла ошибка: {str(e)}")
        msgBox.exec_()

# Создайте кнопку "сохранить"
button = QPushButton('сохранить')
button.clicked.connect(save_data)
layout.addWidget(button)

window.show()
app.exec_()

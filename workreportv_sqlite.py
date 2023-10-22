from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QCompleter
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import sqlite3

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('D:\pqt_app\my_database.db')
c = conn.cursor()

# Создайте приложение PyQt
app = QApplication([])

# Создайте главное окно
window = QWidget()
layout = QVBoxLayout(window)

# Создайте поля для ввода данных
fields = ['участок', 'фамилия', 'шифр детали', 'наименование детали', 'количество деталей', 'операция', 'норма времени на единицу']
entries = {}

for field in fields:
    # Создайте выпадающий список для каждого поля
    label = QLabel(field)
    layout.addWidget(label)
    edit = QLineEdit()
    c.execute(f'SELECT DISTINCT {field} FROM операции')
    data = c.fetchall()
    completer = QCompleter([str(row[0]) for row in data])
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    edit.setCompleter(completer)
    layout.addWidget(edit)
    entries[field] = edit

# Создайте функцию для сохранения данных
def save_data():
    # Сохраните данные в базу данных
    c.execute(f'''
        INSERT INTO операции (участок, фамилия, шифр_детали, наименование_детали, количество_деталей, операция, норма_времени_на_единицу) VALUES 
        ('{entries["участок"].text()}', '{entries["фамилия"].text()}', '{entries["шифр детали"].text()}', '{entries["наименование детали"].text()}', '{entries["количество деталей"].text()}', '{entries["операция"].text()}', {entries["норма времени на единицу"].text()})
    ''')
    conn.commit()
    # Показать сообщение об успешном сохранении
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Данные успешно сохранены!")
    msgBox.exec_()

# Создайте кнопку "сохранить"
button = QPushButton('сохранить')
button.clicked.connect(save_data)
layout.addWidget(button)

window.show()
app.exec_()

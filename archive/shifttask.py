from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QComboBox
import sqlite3
import sys

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('D:/pqt_app/my_db.db')
c = conn.cursor()

# Создайте таблицы, если они еще не существуют
c.execute('CREATE TABLE IF NOT EXISTS участки (id INTEGER PRIMARY KEY, участок TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS работники (id INTEGER PRIMARY KEY, фамилия TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS детали (id INTEGER PRIMARY KEY, шифр_детали TEXT, наименование_детали TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS операции (id INTEGER PRIMARY KEY, участок TEXT, фамилия TEXT, шифр_детали TEXT, наименование_детали TEXT, операция TEXT, норма_времени_на_единицу REAL)')
c.execute('CREATE TABLE IF NOT EXISTS инструкции (id INTEGER PRIMARY KEY, номер_ТБ_инструкции TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS статус (id INTEGER PRIMARY KEY, статус TEXT)')

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Ввод данных")

        self.table = QTableWidget(self)
        self.table.setRowCount(13)
        self.table.setColumnCount(13)
        self.table.setHorizontalHeaderLabels(['рабочий центр', 'ФИО исполнителя', 'статус', 'очередность', 'шифр детали', 'наименование детали', 'операция', 'количество', 'норма времени на ед', 'срок исполнения', '№ инструкции по Б и ОТ', 'подпись в получении сменного задания и инструктажа', 'Отметка о выполнении'])
        self.table.setGeometry(50, 50, 700, 400)

        # Заполните первый столбец выпадающим списком значений из базы данных
        c.execute("SELECT участок FROM участки")
        участки = c.fetchall()
        for row in range(self.table.rowCount()):
            combo = QComboBox()
            for участок in участки:
                combo.addItem(участок[0])
            self.table.setCellWidget(row, 0, combo)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Продолжить ввод")
        self.btn1.setGeometry(50, 500, 150, 50)

        self.btn2 = QPushButton(self)
        self.btn2.setText("Закончить ввод")
        self.btn2.setGeometry(250, 500, 150, 50)

        self.btn3 = QPushButton(self)
        self.btn3.setText("Сохранить")
        self.btn3.setGeometry(450, 500, 150, 50)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

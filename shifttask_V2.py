from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QComboBox
import sqlite3
import sys

# Создайте соединение с базой данных SQLite
conn = sqlite3.connect('my_db2.db')
c = conn.cursor()

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def addRow(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

    def addComboBoxes(self, row):
        # Заполните каждый столбец новой строки выпадающим списком значений из базы данных
        for column in range(3):  # замените 3 на количество столбцов с выпадающими списками
            combo = QComboBox()
            if column == 0:
                c.execute("SELECT участок FROM участки")
            elif column == 1:
                c.execute("SELECT имя FROM работники")
            elif column == 2:
                c.execute("SELECT смена FROM смены")
            items = c.fetchall()
            combo.addItem("")  # добавляем пустой элемент
            for item in items:
                combo.addItem(item[0])
            self.table.setCellWidget(row, column, combo)

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Ввод данных")

        self.table = QTableWidget(self)
        self.table.setRowCount(1)  # начинаем с одной строки
        self.table.setColumnCount(13)
        self.table.setHorizontalHeaderLabels(['рабочий центр', 'ФИО исполнителя', 'смена', 'очередность', 'шифр детали', 'наименование детали', 'операция', 'количество', 'норма времени на ед', 'срок исполнения', '№ инструкции по Б и ОТ', 'подпись в получении сменного задания и инструктажа', 'Отметка о выполнении'])
        self.table.setGeometry(50, 50, 700, 400)

        self.addComboBoxes(0)  # добавляем выпадающие списки в первую строку

        self.btn1 = QPushButton(self)
        self.btn1.setText("Добавить строку")
        self.btn1.clicked.connect(self.addRow)  # подключаем кнопку к функции добавления строки
        self.btn1.clicked.connect(lambda: self.addComboBoxes(self.table.rowCount() - 1))  # добавляем выпадающие списки в новую строку
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

import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Users(object):
    def setupUi(self, Users):

        Users.setObjectName("Users")
        Users.resize(725, 725)
        Users.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.splitter = QtWidgets.QSplitter(Users)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 700, 700))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.Users_2 = QtWidgets.QLineEdit(self.splitter)
        self.Users_2.setAccessibleName("")
        self.Users_2.setAccessibleDescription("")
        self.Users_2.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 75 18pt \"Times New Roman\";")
        self.Users_2.setText("")
        self.Users_2.setObjectName("Users_2")

        self.File = QtWidgets.QLineEdit(self.splitter)
        self.File.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                "font: 75 16pt \"Times New Roman\";")

        self.File.setText("")
        self.File.setObjectName("File")

        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.pushButton.setObjectName("pushButton")

        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setStatusTip("")
        self.tableWidget.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                       "background-color: rgb(127, 127, 127);")
        self.tableWidget.setObjectName("tableWidget")


        self.retranslateUi(Users)
        QtCore.QMetaObject.connectSlotsByName(Users)

    def retranslateUi(self, Users):
        _translate = QtCore.QCoreApplication.translate
        Users.setWindowTitle(_translate("Users", "Users"))

        self.Users_2.setPlaceholderText(_translate("Users", "Вводите названия пользователей "))

        self.File.setPlaceholderText(_translate("Users", "Вводите названия файлов "))

        self.pushButton.setText(_translate("Users", "Сгенерировать таблицу "))
        self.pushButton.clicked.connect(self.Button)

    def Button(self):
        Users = str(self.Users_2.text())
        File = str(self.File.text())

        Usersarr = Users.split()
        Filearr = File.split()

        Rights = ["Запрет", "Полный запрет", "Право на редактирование", "Полный доступ"]

        self.tableWidget.setColumnCount(len(Filearr))
        self.tableWidget.setRowCount(len(Usersarr))

        self.tableWidget.setHorizontalHeaderLabels(Filearr)

        self.tableWidget.setVerticalHeaderLabels(Usersarr)

        for i in range(len(Usersarr)):
            for j in range(len(Filearr)):
                if i == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem("Полный доступ"))
                if i != 0:
                    a = random.randint(0,3)
                    self.tableWidget.setItem(i, j, QTableWidgetItem(Rights[a]))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Users = QtWidgets.QDialog()
    ui = Ui_Users()
    ui.setupUi(Users)
    Users.show()
    sys.exit(app.exec_())

import random

from PIL.Image import item
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Users(object):
    def setupUi(self, Users):

        Users.setObjectName("Users")
        Users.resize(1080, 800)
        Users.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.splitter_2 = QtWidgets.QSplitter(Users)
        self.splitter_2.setGeometry(QtCore.QRect(600, 10, 471, 471))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")

        self.Entrance = QtWidgets.QLineEdit(self.splitter_2)
        self.Entrance.setAccessibleName("")
        self.Entrance.setAccessibleDescription("")
        self.Entrance.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                    "font: 75 14pt \"Times New Roman\";")
        self.Entrance.setText("")
        self.Entrance.setObjectName("Entrance")

        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                        "font: 8pt \"Times New Roman\";\n"
                                        "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.Instructions = QtWidgets.QLineEdit(self.splitter_2)
        self.Instructions.setAccessibleName("")
        self.Instructions.setAccessibleDescription("")
        self.Instructions.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                        "font: 75 18pt \"Times New Roman\";")

        self.Instructions.setText("")
        self.Instructions.setObjectName("Instructions")

        self.pushButtonInstructions = QtWidgets.QPushButton(self.splitter_2)
        self.pushButtonInstructions.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                                  "font: 18pt \"MS Shell Dlg 2\";")
        self.pushButtonInstructions.setObjectName("pushButtonInstructions")

        self.splitter = QtWidgets.QSplitter(Users)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 581, 471))
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
        self.pushButton.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                      "font: 18pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")

        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setStatusTip("")
        self.tableWidget.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                       "background-color: rgb(127, 127, 127);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.widget = QtWidgets.QWidget(Users)
        self.widget.setGeometry(QtCore.QRect(620, 500, 451, 281))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                 "font: 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "font: 14pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.retranslateUi(Users)
        QtCore.QMetaObject.connectSlotsByName(Users)

    def retranslateUi(self, Users):
        _translate = QtCore.QCoreApplication.translate
        Users.setWindowTitle(_translate("Users", "Users"))

        self.Entrance.setPlaceholderText(_translate("Users", "Введите имя пользователя, которое хотите использовать"))

        self.pushButton_2.setText(_translate("Users", "Использовать пользователя"))
        self.pushButton_2.clicked.connect(self.pushButton2)

        self.Instructions.setPlaceholderText(_translate("Users", "Жду ваших указаний > "))

        self.pushButtonInstructions.setText(_translate("Users", "Далее"))
        self.pushButtonInstructions.clicked.connect(self.pushButtonInstructions1)

        self.Users_2.setPlaceholderText(_translate("Users", "Вводите названия пользователей "))

        self.File.setPlaceholderText(_translate("Users", "Вводите названия файлов "))

        self.pushButton.setText(_translate("Users", "Сгенерировать таблицу "))
        self.pushButton.clicked.connect(self.Button)

        self.label_5.setText(_translate("Users", "Жду ваших указаний > read"))

        self.label_4.setText(_translate("Users", "Над каким объектом производится операция? 1"))

        self.label_2.setText(_translate("Users", "Жду ваших указаний > write"))

        self.label.setText(_translate("Users", "Над каким объектом производится операция? 2"))

        self.label_3.setText(_translate("Users", "Жду ваших указаний > grant"))

        self.label_6.setText(_translate("Users", "Право на какой объект передается? 3\n"""))

        self.label_7.setText(_translate("Users", "Какое право передается? read"))

        self.label_8.setText(_translate("Users", "Какому пользователю передается право? Ivan"))

    def Button(self):
        Users = str(self.Users_2.text())
        File = str(self.File.text())

        self.Usersarr = Users.split()
        self.Filearr = File.split()

        self.Rights = ["Полные права", "Чтение", "Запрет", "Чтение, Запись"]

        self.tableWidget.setColumnCount(len(self.Filearr))
        self.tableWidget.setRowCount(len(self.Usersarr))

        self.tableWidget.setHorizontalHeaderLabels(self.Filearr)

        self.tableWidget.setVerticalHeaderLabels(self.Usersarr)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Полные права"))

        for i in range(len(self.Usersarr)):
            for j in range(len(self.Filearr)):
                if i == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem("Полные права"))
                if i != 0:
                    a = random.randint(0, 3)
                    self.tableWidget.setItem(i, j, QTableWidgetItem(self.Rights[a]))

    def pushButton2(self):
        # print(self.tableWidget.item(0, 0).text())
        try:
            self.znach = str(self.Entrance.text())
            if self.znach in self.Usersarr:
                self.Entrance.setText(f"Вы используете пользвателя под именем {self.znach}")
        except:
            pass

    def pushButtonInstructions1(self):
        try:
            self.command = str(self.Instructions.text())
            self.commandarr = self.command.split()

            self.numberUser = self.Usersarr.index(self.znach)
            self.numberFile = self.Filearr.index(self.commandarr[1])

            self.result = self.tableWidget.item(self.numberUser, self.numberFile).text()

            if self.commandarr[0] == "read":
                if self.result != "Запрет":
                    self.Instructions.setText("Успех!")
                if self.result == "Запрет":
                    self.Instructions.setText("Нет прав!")

            if self.commandarr[0] == "write":
                if self.result == "Полные права" or self.result == "Чтение, Запись":
                    self.Instructions.setText("Успех!")
                else:
                    self.Instructions.setText("Нет прав!")

            if self.commandarr[0] == "grant":
                if self.result == "Полные права":
                    self.command4 = self.command.split()
                    if self.commandarr[2] == "read":
                        self.user1 = self.Usersarr.index(self.command4[3])
                        self.file1 = self.Filearr.index(self.command4[1])
                        self.tableWidget.setItem(self.user1, self.file1, QTableWidgetItem("Чтение"))

                    if self.commandarr[2] == "write":
                        self.user1 = self.Usersarr.index(self.command4[3])
                        self.file1 = self.Filearr.index(self.command4[1])
                        self.tableWidget.setItem(self.user1, self.file1, QTableWidgetItem("Чтение, Запись"))
        except:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Users = QtWidgets.QDialog()
    ui = Ui_Users()
    ui.setupUi(Users)
    Users.show()
    sys.exit(app.exec_())

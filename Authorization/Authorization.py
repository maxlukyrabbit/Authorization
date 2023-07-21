import hashlib
import os
import sqlite3
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Registration(object):
    def setupUi(self, Registration):

        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()

        Registration.setObjectName("Registration")
        Registration.resize(400, 308)
        Registration.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.splitter = QtWidgets.QSplitter(Registration)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.login = QtWidgets.QLabel(self.splitter)
        self.login.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 14pt \"Times New Roman\";")

        self.login.setObjectName("login")

        self.loginLine = QtWidgets.QLineEdit(self.splitter)
        self.loginLine.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.loginLine.setText("")
        self.loginLine.setObjectName("loginLine")

        self.password = QtWidgets.QLabel(self.splitter)
        self.password.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Times New Roman\";")
        self.password.setObjectName("password")

        self.passworLine = QtWidgets.QLineEdit(self.splitter)
        self.passworLine.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.passworLine.setText("")
        self.passworLine.setObjectName("passworLine")
        self.passworLine.setEchoMode(QtWidgets.QLineEdit.Password)


        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")

        self.ButtonPassword = QtWidgets.QPushButton(self.splitter)
        self.ButtonPassword.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                          "background-color: rgb(132, 132, 132);\n"
                                          "")

        self.ButtonPassword.setObjectName("ButtonPassword")
        self.ButtonRegistration = QtWidgets.QPushButton(self.splitter)
        self.ButtonRegistration.setMinimumSize(QtCore.QSize(111, 0))
        self.ButtonRegistration.setStyleSheet("font: 8pt \"Times New Roman\";\n"
                                              "background-color: rgb(132, 132, 132);\n"
                                              "font: 75 14pt \"Times New Roman\";\n"
                                              "")
        self.ButtonRegistration.setObjectName("ButtonRegistration")

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)



    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Authorization"))
        self.login.setText(_translate("Registration",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Введите логин</span></p></body></html>"))

        self.loginLine.setPlaceholderText(_translate("Registration", "LOGIN..."))

        self.password.setText(_translate("Registration",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">Введите пароль</span></p></body></html>"))

        self.passworLine.setPlaceholderText(_translate("Registration", "PASSWORD..."))

        self.radioButton.setText(_translate("Registration", "Показать пароль"))
        self.radioButton.clicked.connect(self.radio)

        self.ButtonPassword.setText(_translate("Registration", "Войти"))
        self.ButtonPassword.clicked.connect(self.Success)


        self.ButtonRegistration.setText(_translate("Registration", "Регистрация"))
        self.ButtonRegistration.clicked.connect(self.Registration)

    def radio(self):
        if self.radioButton.isChecked():
            self.passworLine.setEchoMode(not QtWidgets.QLineEdit.Password)
        else:
            self.passworLine.setEchoMode(QtWidgets.QLineEdit.Password)




    def Success(self):

        login = str(self.loginLine.text())
        password0 = str(self.passworLine.text())
        password0hash = hashlib.md5(password0.encode()).hexdigest()

        try:
            password1 = list(self.cur.execute(f"""SELECT password FROM test WHERE login = \'{login}\'"""))[0][0]
            if str(password1) == str(password0hash):
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("И это победа, всё правильно!!!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Введенны не верные данные")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()


        except:
            print("Problem with Data Base")
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("Введены не верные данные")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def Registration(self):
        subprocess.Popen('Registration.exe')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())

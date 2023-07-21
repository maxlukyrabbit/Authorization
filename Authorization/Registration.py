import smtplib
import hashlib
import sqlite3
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)

class Ui_registration(QWidget, object):
    def setupUi(self, registration):

        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()

        registration.setObjectName("registration")
        registration.resize(430, 319)
        registration.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.splitter = QtWidgets.QSplitter(registration)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.gmail = QtWidgets.QLabel(self.splitter)
        self.gmail.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 14pt \"Times New Roman\";")
        self.gmail.setObjectName("gmail")

        self.loginLine = QtWidgets.QLineEdit(self.splitter)
        self.loginLine.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.loginLine.setText("")
        self.loginLine.setObjectName("loginLine")

        self.password1_2 = QtWidgets.QLabel(self.splitter)
        self.password1_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 75 14pt \"Times New Roman\";")
        self.password1_2.setObjectName("password1_2")

        self.passworLine = QtWidgets.QLineEdit(self.splitter)
        self.passworLine.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.passworLine.setText("")
        self.passworLine.setObjectName("passworLine")
        self.passworLine.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password2_2 = QtWidgets.QLabel(self.splitter)
        self.password2_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 75 14pt \"Times New Roman\";")
        self.password2_2.setObjectName("password2_2")

        self.passworLine_2 = QtWidgets.QLineEdit(self.splitter)
        self.passworLine_2.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.passworLine_2.setText("")
        self.passworLine_2.setObjectName("passworLine_2")
        self.passworLine_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")

        self.create = QtWidgets.QPushButton(self.splitter)
        self.create.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                  "background-color: rgb(132, 132, 132);\n"
                                  "")
        self.create.setObjectName("create")

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "registration"))
        self.gmail.setText(_translate("registration", "<html><head/><body><p>Введите почту</p></body></html>"))

        self.loginLine.setPlaceholderText(_translate("registration", "LOGIN..."))

        self.password1_2.setText(_translate("registration",
                                            "<html><head/><body><p><span style=\" font-weight:600;\">Придумайте пароль</span></p></body></html>"))

        self.passworLine.setPlaceholderText(_translate("registration", "PASSWORD..."))

        self.password2_2.setText(_translate("registration",
                                            "<html><head/><body><p><span style=\" font-weight:600;\">Подтвердите пароль</span></p></body></html>"))

        self.passworLine_2.setPlaceholderText(_translate("registration", "PASSWORD..."))

        self.radioButton.setText(_translate("registration", "Показать пароль"))
        self.radioButton.clicked.connect(self.radio1)

        self.create.setText(_translate("registration", "Создать аккаунт"))
        self.create.clicked.connect(self.Registration)


    def radio1(self):
        if self.radioButton.isChecked():
            self.passworLine_2.setEchoMode(not QtWidgets.QLineEdit.Password)
            self.passworLine.setEchoMode(not QtWidgets.QLineEdit.Password)
        else:
            self.passworLine.setEchoMode(QtWidgets.QLineEdit.Password)
            self.passworLine_2.setEchoMode(QtWidgets.QLineEdit.Password)



    def Registration(self):



        login = str(self.loginLine.text())
        password1 = str(self.passworLine.text())
        password1hash = hashlib.md5(password1.encode()).hexdigest()
        password2 = str(self.passworLine_2.text())
        password2hash = hashlib.md5(password2.encode()).hexdigest()





        try:
            if password1hash == password2hash and login != '' and login != ' ':
                rand = str(random.randint(1000, 9999))
                print(rand)

                self.text, self.ok = QInputDialog.getText(self, 'Input Dialog',
                                                'Введите PIN, отправленный на почту:')
                self.sender = "userauthenticationconfirmation@gmail.com"
                self.password = "2005_password_2005"
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.sender, "Ураааааа!")
                print("sdsds")
                if self.ok:
                        if rand == self.text:
                            print("Часть робит")
                            self.cur.execute(f"""INSERT INTO test VALUES (\'{login}\',\'{password2hash}\')""")
                            self.con.commit()
                            msg = QMessageBox()
                            msg.setWindowTitle("Success")
                            msg.setText("Пользователь добавлен")
                            msg.setIcon(QMessageBox.Warning)
                            msg.exec_()

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Введенны не верные данные")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("Введены не верные данные ujtrut")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    registration = QtWidgets.QDialog()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())

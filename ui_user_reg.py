# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_reg.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from argon2 import PasswordHasher
from argon2.low_level import hash_secret, Type


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 510)
        Form.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.Form = Form
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 280, 161, 22))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 420, 151, 51))
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(210, 260, 101, 16))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 210, 71, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 420, 201, 51))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 160, 161, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 110, 161, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 61))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 71, 16))
        self.lineEdit_13 = QLineEdit(Form)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(210, 280, 161, 22))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 101, 16))
        self.lineEdit_14 = QLineEdit(Form)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(210, 330, 161, 22))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 330, 161, 22))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(210, 310, 121, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 90, 71, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 71, 16))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 310, 101, 16))
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 230, 161, 22))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 110, 161, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(210, 230, 161, 22))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 210, 71, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        self.pushButton.clicked.connect(self.sign_up)
        self.pushButton_2.clicked.connect(self.exit)



    def sign_up(self):
        lstname = self.lineEdit.text()
        frtname = self.lineEdit_2.text()
        midname = self.lineEdit_3.text()
        phonenum = self.lineEdit_6.text()
        adress = self.lineEdit_4.text()
        loc = self.lineEdit_5.text()
        password = self.lineEdit_13.text()
        email = self.lineEdit_7.text()
        extra = self.lineEdit_14.text()

        salt = "12345678"
        hashed = hash_secret(
            password.encode("utf-8"),
            salt.encode("utf-8"),
            time_cost=2,
            memory_cost=16,
            parallelism=1,
            hash_len=16,
            type=Type.I
        )
        hash = hashed.decode('utf-8')

        registr = QSqlQuery()
        if not registr.exec(f"""
                INSERT INTO `owners` (`owner_id`, `last_name`, `first_name`, `middle_name`, `address`, `location`, `phone_number`, `email`, `additional_contact`)
                VALUES (NULL, '{lstname}', '{frtname}', '{midname}', '{adress}', '{loc}', '{phonenum}', '{email}', '{extra}');
            """
        ):
            print("Ошибка выполнения запроса:", doc_registr.lastError().text())

        id_check = QSqlQuery()
        if not id_check.exec(f"SELECT owner_id FROM owners WHERE phone_number = '{phonenum}';"):
            print("Ошибка выполнения запроса (id_check):", id_check.lastError().text())
            return

        if id_check.next():
            docs_id = id_check.value(0)
        else:
            print("Помилка")
            return

        insert_login = QSqlQuery()
        if not insert_login.exec(
            f"INSERT INTO users_login (user_id, phone_login, password_hash, user_type, id_in_list) VALUES (NULL, '{phonenum}', '{hash}', 'usr', '{docs_id}');"
        ):
            print("Ошибка выполнения запроса (insert_login):", insert_login.lastError().text())
            return

        self.Form.close()

    def exit(self):
        self.Form.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041c\u0456\u0441\u0442\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0437\u0432\u0456\u0449\u0435", None))
        self.lineEdit_13.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443", None))
        self.lineEdit_14.setText("")
        self.lineEdit_7.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0438\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0406\u043c'\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"email", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441\u0430", None))
    # retranslateUi


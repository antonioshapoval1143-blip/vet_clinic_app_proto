# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empl_reg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget, QMessageBox)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from argon2 import PasswordHasher
from argon2.low_level import hash_secret, Type


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 740)
        Form.setStyleSheet(u"background-color: rgb(171, 171, 171);")
        self.Form = Form
        self.lineEdit_9 = QLineEdit(Form)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(220, 470, 161, 22))
        self.lineEdit_9.setMouseTracking(True)
        self.lineEdit_9.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 590, 151, 51))
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(210, 260, 101, 16))
        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(210, 280, 161, 22))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 101, 16))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(180, 360, 111, 20))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 450, 101, 16))
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 510, 121, 16))
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(30, 470, 141, 22))
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 400, 101, 16))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 400, 171, 16))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 160, 161, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 420, 141, 22))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 590, 211, 51))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 110, 161, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 71, 16))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 360, 89, 20))
        self.radioButton.setChecked(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 210, 71, 16))
        self.lineEdit_10 = QLineEdit(Form)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(220, 420, 161, 22))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(220, 450, 101, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 71, 16))
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 280, 161, 22))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 340, 131, 16))
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 530, 161, 22))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(210, 230, 161, 22))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 90, 71, 16))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 171, 61))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 210, 71, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 110, 161, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 230, 161, 22))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        self.comboBox_2.addItems(
            ["Терапевт загальної практики", "Хірург", "Дерматолог", "Кардіолог", "Офтальмолог", "Ортопед", "Стоматолог",
             "Репродуктолог", "Лаборант-аналітик"])
        self.comboBox_3.addItems(
            ["Повна зайнятість", "Часткова зайнятість", "Позмінна робота", "Виїзди на дім", "Консультації онлайн"])
        self.pushButton.clicked.connect(self.sign_up)
        self.pushButton_2.clicked.connect(self.exit)
        self.radioButton.toggled.connect(self.toggle_lineedit9)

    def sign_up(self):
        lstname = self.lineEdit.text()
        frtname = self.lineEdit_2.text()
        midname = self.lineEdit_3.text()
        phonenum = self.lineEdit_6.text()
        adress = self.lineEdit_4.text()
        loc = self.lineEdit_5.text()
        password = self.lineEdit_8.text()
        animal_type = self.lineEdit_9.text()
        code = self.lineEdit_7.text()
        spec = self.comboBox_2.currentText()
        exp = self.lineEdit_10.text()
        work_format = self.comboBox_3.currentText()

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

        checking = QSqlQuery()
        if not checking.exec(f"SELECT `status` FROM `reg_keys` WHERE `keys` = '{code}';"):
            print("Ошибка выполнения запроса:", checking.lastError().text())
            return

        if checking.next():
            confirm = checking.value(0)
            if confirm == "apr":
                if self.radioButton.isChecked():
                    print("nice")
                    doc_registr = QSqlQuery()
                    if not doc_registr.exec(f"""
                        INSERT INTO `doctors` (`doctor_id`, `last_name`, `first_name`, `middle_name`, `adress`, `location`, `specialization`, `animal_type`, `work_format`, `contact_info`, `experience_years`)
                        VALUES (NULL, '{lstname}', '{frtname}', '{midname}', '{adress}', '{loc}', '{spec}', '{animal_type}', '{work_format}', '{phonenum}', '{exp}');
                    """
                    ):
                        print("Ошибка выполнения запроса:", doc_registr.lastError().text())

                    id_check = QSqlQuery()
                    if not id_check.exec(f"SELECT doctor_id FROM doctors WHERE contact_info = '{phonenum}';"):
                        print("Ошибка выполнения запроса (id_check):", id_check.lastError().text())
                        return

                    if id_check.next():
                        docs_id = id_check.value(0)
                    else:
                        print("Ключ не найден в таблице.")
                        return

                    insert_login = QSqlQuery()
                    if not insert_login.exec(
                            f"INSERT INTO users_login (user_id, phone_login, password_hash, user_type, id_in_list) VALUES (NULL, '{phonenum}', '{hash}', 'doc', '{docs_id}');"
                    ):
                        print("Ошибка выполнения запроса (insert_login):", insert_login.lastError().text())
                        return
                else:
                    adm_registr = QSqlQuery()
                    if not adm_registr.exec(f"""
                        INSERT INTO `admins` (`admin_id`, `last_name`, `first_name`, `middle_name`, `specialization`, `adress`, `location`, `phone_number`)
                        VALUES (NULL, '{lstname}', '{frtname}', '{midname}', '{spec}', '{adress}', '{loc}', '{phonenum}');
                    """
                    ):
                        print("Ошибка выполнения запроса:", adm_registr.lastError().text())

                    id_check = QSqlQuery()
                    if not id_check.exec(f"SELECT admin_id FROM admins WHERE phone_number = '{phonenum}';"):
                        print("Ошибка выполнения запроса (id_check):", id_check.lastError().text())
                        return

                    if id_check.next():
                        adm_id = id_check.value(0)
                    else:
                        print("Ключ не найден в таблице.")
                        return

                    insert_login = QSqlQuery()
                    if not insert_login.exec(
                            f"INSERT INTO users_login (user_id, phone_login, password_hash, user_type, id_in_list) VALUES (NULL, '{phonenum}', '{hash}', 'adm', '{adm_id}');"
                    ):
                        print("Ошибка выполнения запроса (insert_login):", insert_login.lastError().text())
                        return
                self.Form.close()

            else:
                QMessageBox.critical(self.Form, "Помилка", "Ваш код підтвердження не є дійсним. Введіть інший або отримайте його від адміністрації")

        else:
            QMessageBox.critical(self.Form, "Помилка", "Ваш код підтвердження не є дійсним. Введіть інший або отримайте його від адміністрації")

    def toggle_lineedit9(self, checked):
        if checked:
            self.comboBox_2.clear()
            self.lineEdit_9.show()
            self.lineEdit_10.show()
            self.comboBox_3.show()
            self.label_9.show()
            self.label_11.show()
            self.label_12.show()
            self.comboBox_2.addItems(
                ["Терапевт загальної практики", "Хірург", "Дерматолог", "Кардіолог", "Офтальмолог", "Ортопед",
                 "Стоматолог", "Репродуктолог", "Лаборант-аналітик"])

        else:
            self.comboBox_2.clear()
            self.lineEdit_9.hide()
            self.lineEdit_10.hide()
            self.comboBox_3.hide()
            self.label_9.hide()
            self.label_11.hide()
            self.label_12.hide()
            self.comboBox_2.addItems(["Адміністратор", "Бухгалтер"])

    def exit(self):
        self.Form.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_8.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u043c\u0456\u043d\u0456\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0440\u043e\u0431\u043e\u0442\u0438", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u0434 \u043f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u0456\u0437\u0430\u0446\u0456\u044f", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0420\u0456\u0432\u0435\u043d\u044c \u043a\u0432\u0430\u043b\u0456\u0444\u0456\u043a\u0430\u0446\u0456\u0457 (\u0432 \u0440\u043e\u043a\u0430\u0445)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0437\u0432\u0456\u0449\u0435", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u041b\u0456\u043a\u0430\u0440", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041c\u0456\u0441\u0442\u043e", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0442\u0432\u0430\u0440\u0438\u043d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.lineEdit_6.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0430\u0434\u0430", None))
        self.lineEdit_7.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0406\u043c'\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441\u0430", None))
    # retranslateUi


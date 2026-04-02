# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stress_test.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QWidget, QMessageBox)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(266, 300)
        self.Form = Form
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 200, 91, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 200, 91, 31))
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(140, 100, 101, 22))
        self.spinBox.setMaximum(1000)
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(140, 40, 101, 20))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(8, 40, 121, 20))
        self.radioButton_2.setChecked(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 111, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        self.stress_point = 1
        self.result_output = []
        self.pushButton.clicked.connect(self.run_stress_test)
        self.pushButton_2.clicked.connect(self.exit)
        self.radioButton.toggled.connect(self.chose_test_type)
        self.radioButton_2.toggled.connect(self.chose_test_type)

        self.stress_query = f"""
        INSERT INTO test_table VALUES (NULL, 'stressssssssssssssss', '{self.stress_point}');
        """
        tq = QSqlQuery()
        if not tq.exec("""
        CREATE TABLE IF NOT EXISTS test_table (
            stress_id INT AUTO_INCREMENT PRIMARY KEY,
            stress_name VARCHAR(255),
            stress_point INT
        );
        """):
            print(":(")


    def chose_test_type(self):
        tq = QSqlQuery()

        if self.radioButton_2.isChecked():
            if not tq.exec("""
            CREATE TABLE IF NOT EXISTS test_table (
                stress_id INT AUTO_INCREMENT PRIMARY KEY,
                stress_name VARCHAR(255),
                stress_point INT
            );
            """):
                print("0")
        elif self.radioButton.isChecked():
            if not tq.exec("""
            DROP TABLE IF EXISTS test_table;
            """):
                print("0")


    def run_stress_test(self):
        try:
            # Отримуємо кількість запитів
            num_requests = int(self.spinBox.value())
            if num_requests <= 0:
                #self.result_output.setText(
                QMessageBox.warning(self.Form, "", "Введіть додатнє число!")
                return

            self.result_output.clear()
            self.result_output.append("Початок стрес-тесту...")

            # Початок вимірювання часу
            start_time = time.time()

            query = QSqlQuery()
            success_count = 0
            error_count = 0

            for i in range(num_requests):
                if query.exec(self.stress_query):
                    success_count += 1
                    self.stress_point = success_count
                else:
                    error_count += 1

            # Кінець вимірювання часу
            end_time = time.time()
            total_time = end_time - start_time

            # Виведення результатів
            self.result_output.append(f"\nТест завершено!")
            self.result_output.append(f"Успішних запитів: {success_count}")
            self.result_output.append(f"Помилок: {error_count}")
            self.result_output.append(f"Загальний час: {total_time:.5f} секунд")
            self.result_output.append(f"Запитів за секунду: {success_count / total_time:.2f}")

        except ValueError:
            QMessageBox.warning(self.Form, "ValueError", "Введіть коректне число!")
        except Exception as e:
            QMessageBox.warning(self.Form, "Exception", f"Помилка: {str(e)}")

        QMessageBox.information(self.Form, "Stress test", f'''
        {self.result_output[0]}
        {self.result_output[1]}
        {self.result_output[2]}
        {self.result_output[3]}
        {self.result_output[4]}
        {self.result_output[5]}
        ''')
        print(self.result_output[4])


    def exit(self):
        exit_query = "DROP TABLE IF EXISTS test_table;"
        exit_query_exec = QSqlQuery()
        if not exit_query_exec.exec(exit_query):
            print("something went wrong")
        self.Form.close()



    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u0406\u0437 \u043f\u043e\u043c\u0438\u043b\u043a\u0430\u043c\u0438", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u043f\u0456\u0448\u043d\u0435 \u0434\u043e\u0434\u0430\u0432\u0430\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u0456\u0432</span></p></body></html>", None))
    # retranslateUi


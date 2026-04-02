# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 300)
        Dialog.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.lineEdit_8 = QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(120, 50, 113, 22))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_9 = QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(120, 80, 113, 22))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_11 = QLineEdit(Dialog)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(310, 50, 31, 22))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(280, 50, 21, 16))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 110, 49, 16))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 80, 49, 16))
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 80, 41, 20))
        self.lineEdit_10 = QLineEdit(Dialog)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(120, 110, 113, 22))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 50, 49, 16))
        self.lineEdit_12 = QLineEdit(Dialog)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(310, 80, 31, 22))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 190, 121, 51))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 190, 121, 51))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 141, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u043a", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0438\u0447\u043a\u0430", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0434\u0430", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0433\u0430, \u043a\u0433", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0442\u0432\u0430\u0440\u0438\u043d\u043a\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0441\u0432\u043e\u044e \u0442\u0432\u0430\u0440\u0438\u043d\u043a\u0443", None))
    # retranslateUi


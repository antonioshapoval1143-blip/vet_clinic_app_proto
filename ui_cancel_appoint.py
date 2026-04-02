# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cancel_appoint.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(561, 171)
        Dialog.setStyleSheet(u"background-color: rgb(188, 188, 188);")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 40, 191, 22))
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 20, 81, 16))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 90, 171, 51))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 93, 171, 51))
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 40, 81, 21))
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 20, 81, 16))
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 20, 161, 16))
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(380, 40, 151, 21))
        self.label_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 40, 49, 21))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 20, 49, 16))
        self.comboBox.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label_15.raise_()
        self.label.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_14.raise_()

        self.retranslateUi(Dialog)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0438\u0441\u0443</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0438\u0441\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438 \u0437\u0430\u043f\u0438\u0441 \u043f\u0430\u0446\u0456\u0454\u043d\u0442\u0430", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">0000.00.00</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0446\u0456\u0454\u043d\u0442", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041b\u0456\u043a\u0430\u0440</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">_</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">_</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0438\u0441", None))
    # retranslateUi


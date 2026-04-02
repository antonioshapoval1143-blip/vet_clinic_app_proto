# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appnt_pet.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QPushButton, QSizePolicy, QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(552, 394)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 310, 181, 61))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 310, 181, 61))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 80, 181, 31))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(270, 120, 181, 31))
        self.timeEdit = QTimeEdit(Form)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(280, 250, 118, 22))
        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(140, 250, 110, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 90, 111, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 170, 111, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 230, 49, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 230, 49, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 20, 111, 20))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 130, 111, 16))
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(270, 160, 181, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u043f\u0435\u0442\u043e\u043c\u0446\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u043b\u0456\u043a\u0430\u0440\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u043d\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u0438 \u0442\u0432\u0430\u0440\u0438\u043d\u043a\u0443", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u0438\u0441\u044f \u0434\u043e...", None))
    # retranslateUi


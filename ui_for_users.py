# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'for_users.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(785, 556)
        Form.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 350, 581, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 440, 211, 41))
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(90, 30, 601, 311))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 410, 191, 41))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(530, 440, 201, 41))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(300, 460, 191, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u043a\u043e\u043d\u0430\u0442\u0438 \u0437\u0430\u043f\u0438\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u0438\u0441\u044c \u043d\u0430 \u043f\u0440\u0438\u0439\u043e\u043c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438 \u0446\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438 \u043f\u0440\u0438\u0439\u043e\u043c", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 514)
        Form.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 440, 161, 61))
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(50, 0, 521, 421))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 440, 161, 61))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0440\u044f\u0434\u043e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'query_for_admin.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(951, 574)
        Form.setStyleSheet(u"background-color: rgb(181, 181, 181);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 440, 151, 41))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 470, 371, 41))
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 10, 901, 401))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 440, 181, 16))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 490, 151, 41))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 440, 111, 41))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(630, 490, 111, 41))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(840, 473, 75, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u043a\u043e\u043d\u0430\u0442\u0438 \u0437\u0430\u043f\u0438\u0442", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0437\u0432\u0456\u0442", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041b\u0456\u043a\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi


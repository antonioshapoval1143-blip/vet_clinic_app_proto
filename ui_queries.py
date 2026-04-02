# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'queries.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1259, 512)
        Dialog.setStyleSheet(u"background-color: rgb(154, 154, 154);")
        self.tableView_2 = QTableView(Dialog)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(40, 40, 501, 321))
        self.tableView_2.setTabletTracking(False)
        self.tableView_2.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);")
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QRect(700, 50, 381, 31))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(800, 110, 181, 51))
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(800, 180, 181, 61))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(800, 260, 181, 61))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1144, 10, 101, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043f\u0440\u0430\u0432\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0442", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0444\u043e\u0440\u043c\u0443\u0432\u0430\u0442\u0438 \u0437\u0432\u0456\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u0434\u0430\u043d\u0456", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438 \u0446\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi


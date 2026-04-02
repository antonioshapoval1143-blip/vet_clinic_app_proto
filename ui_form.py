# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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

class Ui_DBUI(object):
    def setupUi(self, DBUI):
        if not DBUI.objectName():
            DBUI.setObjectName(u"DBUI")
        DBUI.resize(1281, 600)
        DBUI.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        DBUI.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.pushButton = QPushButton(DBUI)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 210, 171, 41))
        self.tableView = QTableView(DBUI)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(265, 111, 911, 321))
        self.tableView.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(222, 222, 222);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.comboBox = QComboBox(DBUI)
        self.comboBox.addItem(u"users_login")
        self.comboBox.addItem(u"doctors")
        self.comboBox.addItem(u"owners")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 110, 141, 31))
        self.pushButton_2 = QPushButton(DBUI)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 260, 171, 51))
        self.pushButton_3 = QPushButton(DBUI)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1124, 20, 111, 51))
        self.pushButton_4 = QPushButton(DBUI)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(70, 340, 151, 51))

        self.retranslateUi(DBUI)

        QMetaObject.connectSlotsByName(DBUI)
    # setupUi

    def retranslateUi(self, DBUI):
        DBUI.setWindowTitle(QCoreApplication.translate("DBUI", u"DBUI", None))
        self.pushButton.setText(QCoreApplication.translate("DBUI", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("DBUI", u"patients", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("DBUI", u"treatments", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("DBUI", u"appointments", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("DBUI", u"admins", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("DBUI", u"reg_keys", None))

        self.pushButton_2.setText(QCoreApplication.translate("DBUI", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("DBUI", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438 \u0446\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButton_4.setText(QCoreApplication.translate("DBUI", u"\u0421\u0442\u0440\u0435\u0441 \u0442\u0435\u0441\u0442", None))
    # retranslateUi


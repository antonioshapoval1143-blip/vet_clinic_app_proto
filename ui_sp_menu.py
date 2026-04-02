# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sp_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(513, 399)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 70, 121, 51))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 150, 121, 51))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 310, 121, 51))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 70, 89, 20))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(150, 70, 111, 20))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(90, 130, 76, 20))
        self.checkBox.setChecked(False)
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(90, 150, 101, 20))
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(90, 170, 76, 20))
        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(90, 190, 76, 20))
        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(90, 210, 76, 20))
        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(90, 230, 76, 20))
        self.checkBox_7 = QCheckBox(Form)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(90, 270, 81, 20))
        self.checkBox_8 = QCheckBox(Form)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(90, 250, 91, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0431\u0435\u043a\u0430\u043f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0431\u0435\u043a\u0430\u043f", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0439\u0442\u0438 \u0437 \u043c\u0435\u043d\u044e", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u044f \u0431\u0430\u0437\u0430 \u0434\u0430\u043d\u0438\u0445", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u041e\u043a\u0440\u0435\u043c\u0456 \u0442\u0430\u0431\u043b\u0438\u0446\u0456", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"admins", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"appointments", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"doctors", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"owners", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"patients", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"reg_keys", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"users_login", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"treatments", None))
    # retranslateUi


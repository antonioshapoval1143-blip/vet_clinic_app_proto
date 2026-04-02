# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg_type.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
from ui_empl_reg import Ui_Form as reg_empl
from ui_user_reg import Ui_Form as reg_user


class Ui_RegDialog(object):
    def setupUi(self, RegDialog):
        if not RegDialog.objectName():
            RegDialog.setObjectName(u"RegDialog")
        RegDialog.resize(377, 180)
        self.dialog = RegDialog
        self.pushButton = QPushButton(RegDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 110, 75, 24))
        self.pushButton_2 = QPushButton(RegDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 110, 75, 24))
        self.pushButton_3 = QPushButton(RegDialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(260, 110, 75, 24))
        self.label = QLabel(RegDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 241, 61))

        self.retranslateUi(RegDialog)

        QMetaObject.connectSlotsByName(RegDialog)
    # setupUi

        self.pushButton.clicked.connect(self.user_registration)
        self.pushButton_2.clicked.connect(self.empl_registration)
        self.pushButton_3.clicked.connect(self.cancel_button)


    def user_registration(self):
        self.dialog.close()
        dialog = QDialog()
        re = reg_user()
        re.setupUi(dialog)
        dialog.exec()

    def empl_registration(self):
        self.dialog.close()
        dialog = QDialog()
        re = reg_empl()
        re.setupUi(dialog)
        dialog.exec()

    def cancel_button(self):
        self.dialog.close()

    def retranslateUi(self, RegDialog):
        RegDialog.setWindowTitle(QCoreApplication.translate("RegDialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("RegDialog", u"\u041a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447", None))
        self.pushButton_2.setText(QCoreApplication.translate("RegDialog", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a", None))
        self.pushButton_3.setText(QCoreApplication.translate("RegDialog", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("RegDialog", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f \u044f\u043a...", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1108, 548)
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(280, 80, 791, 411))
        self.tableWidget.setFrameShape(QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 170, 171, 61))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 70, 141, 16))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 240, 171, 61))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 90, 171, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID \u043f\u0430\u0446\u0456\u0454\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u0438\u0447\u043a\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0440\u043e\u0434\u0430", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0412\u0456\u043a(\u0440\u043e\u043a\u0456\u0432)", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0412\u0430\u0433\u0430(\u043a\u0433)", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0441\u043d\u0438\u043a ", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"000001", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u0428\u0435\u0440\u0440\u0456", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u041a\u0456\u0442", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0439\u0441\u044c\u043a\u0430", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"\u0428\u0430\u043f\u043e\u0432\u0430\u043b \u0410\u043d\u0442\u043e\u043d \u041e\u043b\u0435\u043a\u0441\u0456\u0439\u043e\u0432\u0438\u0447", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0434\u0430\u043d\u0456", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0456 \u0437 \u0434\u0430\u043d\u0438\u043c\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0434\u0430\u043d\u0456", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u041f\u0430\u0446\u0456\u0454\u043d\u0442\u0438", None))

    # retranslateUi


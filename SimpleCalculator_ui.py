# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SimpleCalculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(281, 325)
        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(20, 280, 91, 31))
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 240, 41, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 240, 41, 31))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 240, 41, 31))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 200, 41, 31))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 200, 41, 31))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 200, 41, 31))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 160, 41, 31))
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(120, 160, 41, 31))
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(70, 160, 41, 31))
        self.pushButton_point = QPushButton(Form)
        self.pushButton_point.setObjectName(u"pushButton_point")
        self.pushButton_point.setGeometry(QRect(120, 280, 41, 31))
        self.pushButton_sum = QPushButton(Form)
        self.pushButton_sum.setObjectName(u"pushButton_sum")
        self.pushButton_sum.setGeometry(QRect(170, 280, 41, 31))
        self.pushButton_sub = QPushButton(Form)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        self.pushButton_sub.setGeometry(QRect(170, 240, 41, 31))
        self.pushButton_muti = QPushButton(Form)
        self.pushButton_muti.setObjectName(u"pushButton_muti")
        self.pushButton_muti.setGeometry(QRect(170, 200, 41, 31))
        self.pushButton_div = QPushButton(Form)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setGeometry(QRect(170, 160, 41, 31))
        self.pushButton_done = QPushButton(Form)
        self.pushButton_done.setObjectName(u"pushButton_done")
        self.pushButton_done.setGeometry(QRect(220, 240, 41, 71))
        self.pushButton_right = QPushButton(Form)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setGeometry(QRect(170, 120, 41, 31))
        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(70, 120, 41, 31))
        self.pushButton_del = QPushButton(Form)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setGeometry(QRect(20, 120, 41, 31))
        self.pushButton_left = QPushButton(Form)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setGeometry(QRect(120, 120, 41, 31))
        self.pushButton_output = QPushButton(Form)
        self.pushButton_output.setObjectName(u"pushButton_output")
        self.pushButton_output.setGeometry(QRect(220, 120, 41, 111))
        self.result = QTextBrowser(Form)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(20, 60, 241, 41))
        self.result_history = QTextBrowser(Form)
        self.result_history.setObjectName(u"result_history")
        self.result_history.setGeometry(QRect(20, 10, 241, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7b80\u6613\u8ba1\u7b97\u5668", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_point.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_sum.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_muti.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_done.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_right.setText(QCoreApplication.translate("Form", u")", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"clear", None))
        self.pushButton_del.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.pushButton_left.setText(QCoreApplication.translate("Form", u"(", None))
        self.pushButton_output.setText(QCoreApplication.translate("Form", u"\u5bfc\n"
"\u51fa\n"
"\u5386\n"
"\u53f2\n"
"\u8bb0\n"
"\u5f55", None))
        self.result.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.result_history.setPlaceholderText(QCoreApplication.translate("Form", u"\u5386\u53f2\u8bb0\u5f55\u4f1a\u51fa\u73b0\u5728\u8fd9\u91cc", None))
    # retranslateUi


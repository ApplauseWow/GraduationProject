# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_win.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_warning_win(object):
    def setupUi(self, warning_win):
        warning_win.setObjectName("warning_win")
        warning_win.resize(416, 279)
        self.horizontalLayoutWidget = QtWidgets.QWidget(warning_win)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 391, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.warning = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.warning.setText("")
        self.warning.setObjectName("warning")
        self.horizontalLayout.addWidget(self.warning)
        self.words = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.words.setFont(font)
        self.words.setObjectName("words")
        self.horizontalLayout.addWidget(self.words)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(warning_win)
        QtCore.QMetaObject.connectSlotsByName(warning_win)

    def retranslateUi(self, warning_win):
        _translate = QtCore.QCoreApplication.translate
        warning_win.setWindowTitle(_translate("warning_win", "Dialog"))
        self.words.setText(_translate("warning_win", "识别失败"))


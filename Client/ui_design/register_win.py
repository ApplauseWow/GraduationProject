# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_win.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_win(object):
    def setupUi(self, register_win):
        register_win.setObjectName("register_win")
        register_win.resize(431, 334)
        self.bt_reg = QtWidgets.QPushButton(register_win)
        self.bt_reg.setGeometry(QtCore.QRect(290, 60, 121, 41))
        self.bt_reg.setObjectName("bt_reg")
        self.bt_again = QtWidgets.QPushButton(register_win)
        self.bt_again.setGeometry(QtCore.QRect(290, 120, 121, 41))
        self.bt_again.setObjectName("bt_again")
        self.bt_cancel = QtWidgets.QPushButton(register_win)
        self.bt_cancel.setGeometry(QtCore.QRect(290, 180, 121, 41))
        self.bt_cancel.setObjectName("bt_cancel")
        self.process = QtWidgets.QProgressBar(register_win)
        self.process.setGeometry(QtCore.QRect(40, 260, 221, 23))
        self.process.setProperty("value", 24)
        self.process.setObjectName("process")
        self.capture_pic = QtWidgets.QLabel(register_win)
        self.capture_pic.setGeometry(QtCore.QRect(50, 70, 201, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_pic.sizePolicy().hasHeightForWidth())
        self.capture_pic.setSizePolicy(sizePolicy)
        self.capture_pic.setObjectName("capture_pic")

        self.retranslateUi(register_win)
        QtCore.QMetaObject.connectSlotsByName(register_win)

    def retranslateUi(self, register_win):
        _translate = QtCore.QCoreApplication.translate
        register_win.setWindowTitle(_translate("register_win", "Dialog"))
        self.bt_reg.setText(_translate("register_win", "确定注册"))
        self.bt_again.setText(_translate("register_win", "重新拍照"))
        self.bt_cancel.setText(_translate("register_win", "取消注册"))
        self.capture_pic.setText(_translate("register_win", "照片"))


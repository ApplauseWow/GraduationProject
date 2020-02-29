# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'id_info_win.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_id_info_win(object):
    def setupUi(self, id_info_win):
        id_info_win.setObjectName("id_info_win")
        id_info_win.resize(443, 304)
        id_info_win.setStyleSheet("")
        self.b_login = QtWidgets.QPushButton(id_info_win)
        self.b_login.setGeometry(QtCore.QRect(322, 240, 90, 40))
        self.b_login.setStyleSheet("QPushButton{"
"                   background-color:rgba(255,165,0,80);"
"                   border-style:outset;                  "
"                   border-width:4px;                     "
"                   border-radius:10px;                "
"                   border-color:rgba(255,255,255,30);   "
"                   font:bold 18px;                    "
"                   color:rgba(0,0,0,100);                "
"                   padding:6px;                       "
"                   }"
"                   QPushButton:pressed{"
"                   background-color:rgba(255,165,0,200);"
"                   border-color:rgba(255,255,255,30);"
"                   border-style:inset;"
"                   color:rgba(0,0,0,100);"
"                   }"
"                   QPushButton:hover{"
"                   background-color:rgba(255,165,0,100);"
"                   border-color:rgba(255,255,255,200);"
"                   color:rgba(0,0,0,200);"
"                   }")
        self.b_login.setObjectName("b_login")
        self.b_wrong = QtWidgets.QPushButton(id_info_win)
        self.b_wrong.setGeometry(QtCore.QRect(231, 240, 90, 40))
        self.b_wrong.setStyleSheet("QPushButton{"
"                   background-color:rgba(255,165,0,80);"
"                   border-style:outset;                  "
"                   border-width:4px;                     "
"                   border-radius:10px;                "
"                   border-color:rgba(255,255,255,30);   "
"                   font:bold 18px;                    "
"                   color:rgba(0,0,0,100);                "
"                   padding:6px;                       "
"                   }"
"                   QPushButton:pressed{"
"                   background-color:rgba(255,165,0,200);"
"                   border-color:rgba(255,255,255,30);"
"                   border-style:inset;"
"                   color:rgba(0,0,0,100);"
"                   }"
"                   QPushButton:hover{"
"                   background-color:rgba(255,165,0,100);"
"                   border-color:rgba(255,255,255,200);"
"                   color:rgba(0,0,0,200);"
"                   }")
        self.b_wrong.setObjectName("b_wrong")
        self.b_ok = QtWidgets.QPushButton(id_info_win)
        self.b_ok.setGeometry(QtCore.QRect(140, 240, 90, 40))
        self.b_ok.setStyleSheet("QPushButton{"
"                   background-color:rgba(255,165,0,80);"
"                   border-style:outset;                  "
"                   border-width:4px;                     "
"                   border-radius:10px;                "
"                   border-color:rgba(255,255,255,30);   "
"                   font:bold 18px;                    "
"                   color:rgba(0,0,0,100);                "
"                   padding:6px;                       "
"                   }"
"                   QPushButton:pressed{"
"                   background-color:rgba(255,165,0,200);"
"                   border-color:rgba(255,255,255,30);"
"                   border-style:inset;"
"                   color:rgba(0,0,0,100);"
"                   }"
"                   QPushButton:hover{"
"                   background-color:rgba(255,165,0,100);"
"                   border-color:rgba(255,255,255,200);"
"                   color:rgba(0,0,0,200);"
"                   }")
        self.b_ok.setObjectName("b_ok")
        self.l_name = QtWidgets.QLabel(id_info_win)
        self.l_name.setGeometry(QtCore.QRect(76, 68, 120, 35))
        self.l_name.setObjectName("l_name")
        self.user_type = QtWidgets.QLabel(id_info_win)
        self.user_type.setGeometry(QtCore.QRect(200, 150, 223, 35))
        self.user_type.setObjectName("user_type")
        self.user_name = QtWidgets.QLabel(id_info_win)
        self.user_name.setGeometry(QtCore.QRect(200, 68, 223, 35))
        self.user_name.setObjectName("user_name")
        self.user_id = QtWidgets.QLabel(id_info_win)
        self.user_id.setGeometry(QtCore.QRect(200, 109, 223, 35))
        self.user_id.setObjectName("user_id")
        self.l_id = QtWidgets.QLabel(id_info_win)
        self.l_id.setGeometry(QtCore.QRect(76, 109, 120, 35))
        self.l_id.setObjectName("l_id")
        self.l_type = QtWidgets.QLabel(id_info_win)
        self.l_type.setGeometry(QtCore.QRect(76, 150, 120, 35))
        self.l_type.setObjectName("l_type")
        self.retranslateUi(id_info_win)
        QtCore.QMetaObject.connectSlotsByName(id_info_win)

    def retranslateUi(self, id_info_win):
        _translate = QtCore.QCoreApplication.translate
        id_info_win.setWindowTitle(_translate("id_info_win", "Dialog"))
        self.b_login.setText(_translate("id_info_win", "进入系统"))
        self.b_wrong.setText(_translate("id_info_win", "有误重试"))
        self.b_ok.setText(_translate("id_info_win", "确定"))
        self.l_name.setText(_translate("id_info_win", "姓名"))
        self.user_type.setText(_translate("id_info_win", "xxxxx"))
        self.user_name.setText(_translate("id_info_win", "xxxxx"))
        self.user_id.setText(_translate("id_info_win", "xxxxx"))
        self.l_id.setText(_translate("id_info_win", "工号/学号"))
        self.l_type.setText(_translate("id_info_win", "用户类型"))


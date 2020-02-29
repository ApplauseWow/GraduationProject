# -*-coding:utf-8-*-
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDialog, QLabel, QLCDNumber
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import time

from main_win import Ui_MainWindow
from id_info_win import Ui_id_info_win


class DIYLabel(QLabel):
    """
    自定义Label控件
    拥有点击事件响应的Label
    """

    clicked = pyqtSignal()  # 定义信号量

    def mouseReleaseEvent(self, QMouseEvent):
        """
        鼠标松开时触发
        :param QMouseEvent:鼠标事件
        :return: None
        """

        if QMouseEvent.button() == Qt.LeftButton:  # 鼠标左键松开
            self.clicked.emit()  # 发送信号



class MainWindow(Ui_MainWindow, QMainWindow):
    """
    主界面二次设计
    """

    def __init__(self):
        super(MainWindow, self).__init__()

        # 获取桌面尺寸
        desktop = QApplication.desktop()
        desk_width = desktop.screenGeometry().width()
        desk_height = desktop.screenGeometry().height()

        # 摄像头图像设置
        self.frame = DIYLabel(self)
        self.frame.setGeometry(0, 0, desk_width, desk_height)

        self.setupUi(self)

        # 按钮定位
        buttons = [self.att_rec, self.face_login, self.face_rec, self.face_reg]
        map(lambda x: x.move(desk_width*0.80, desk_height*0.33+buttons.index(x)*(x.height()+8)), buttons)
        map(lambda x: x.raise_(), buttons)

        # 设置时钟
        self.clock = QLCDNumber(self)
        self.clock.setDigitCount(10)
        self.clock.setMode(QLCDNumber.Dec)
        self.clock.setSegmentStyle(QLCDNumber.Flat)
        self.clock.display(time.strftime("%X", time.localtime()))
        self.clock.resize(280, 120)
        self.clock.move(50, desk_height - 30 - self.clock.height())
        self.clock.setStyleSheet("QLCDNumber{color:rgba(255,0,0,100);}")

        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏窗口
        self.showFullScreen()  # 窗体全屏


class InfoWindow(Ui_id_info_win, QDialog):
    """
    个人信息窗口二次设计
    """

    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)

        # 获取桌面尺寸
        desktop = QApplication.desktop()
        desk_width = desktop.availableGeometry().width()
        desk_height = desktop.availableGeometry().height()

        # 窗体定位
        self.move(int(desk_width*0.3), int(desk_height*0.3))

        # 修改label样式
        labels = [self.l_id, self.l_name, self.l_type, self.user_id, self.user_name, self.user_type]
        map(lambda x: x.setStyleSheet("QLabel{"
                                      "                   background-color:rgba(255,165,0,150);"
                                      "                   border-style:outset;                  "
                                      "                   border-width:4px;                     "
                                      "                   border-radius:10px;                "
                                      "                   border-color:rgba(255,255,255,30);   "
                                      "                   font:bold 18px;                    "
                                      "                   color:rgb(255,255,255);                "
                                      "                   padding:6px;                       "
                                      "                   }"),labels)

        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 影藏窗口


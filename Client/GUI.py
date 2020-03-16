# -*-coding:utf-8-*-
import time
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from ui_design.ui_finish import *


class SysHome(MainWindow):
    """
    主界面
    """

    def __init__(self):
        super(SysHome, self).__init__()

        # 设置定时器
        self.timer_clock = QTimer()
        self.timer_clock.setInterval(1000)
        self.timer_clock.start()
        self.timer_clock.timeout.connect(self.update_time)

    def update_time(self):
        """
        更新时间
        :return:None
        """

        self.clock.display(time.strftime("%X", time.localtime()))


class Warning(WarningWindow):
    """
    警告提醒窗
    """

    def __init__(self):
        super(Warning, self).__init__()
        # 设置定时器
        self.time_count = QTimer()
        self.time_count.setInterval(1500)
        self.time_count.start()
        self.time_count.timeout.connect(self.timeout_close)

    def timeout_close(self):
        """
        倒计时关闭此窗口
        :return: None
        """

        self.close()


class Register():
    """
    人脸注册窗口
    """

    def __init__(self):
        super(Register, self).__init__()


class MyInfo(InfoWindow):
    """
    考勤窗口｜个人信息显示窗口
    """

    def __init__(self):
        super(MyInfo, self).__init__()


class Management(ManagementWindow):
    """
    资源管理窗口
    """

    def __init__(self, user_id, user_type):
        super(Management, self).__init__(user_id, user_type)
        self.bt_close.clicked.connect(self.showPage)

    def showPage(self):
        y = QGridLayout()
        w = QWidget()
        y.addWidget(self.page(), 5, 3, 5, 8)
        y.addWidget(self.page(), 5, 11, 5, 8)
        y.setRowStretch(1,1)
        y.setRowStretch(5, 8)
        y.setRowStretch(12, 1)
        w.setLayout(y)
        self.right_layout.addWidget(w)

    class page(Pagination):

        def __init__(self):
            Pagination.__init__(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_ = Management(201610414206, 1)
    win_.show()
    sys.exit(app.exec_())
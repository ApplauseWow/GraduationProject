# -*-coding:utf-8-*-
import time
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from ui_design.ui_finish import MainWindow, InfoWindow, WarningWindow


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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_ = Warning()
    win_.show()
    sys.exit(app.exec_())
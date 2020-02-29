# -*-coding:utf-8-*-
import time
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from ui_design.ui_finish import MainWindow, InfoWindow


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
        self.timer_clock.timeout.connect(self._update_time)

    def _update_time(self):
        self.clock.display(time.strftime("%X", time.localtime()))
        print(time.strftime("%X", time.localtime()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_ = SysHome()
    win_.show()
    sys.exit(app.exec_())
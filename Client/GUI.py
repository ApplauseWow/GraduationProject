# -*-coding:utf-8-*-
import time
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from ui_design.ui_finish import *
from TypesEnum import *


class Page(Pagination):
    """
    数据表分页，构建基本事件响应函数
    Management中多个控件需要重写此类
    """

    def __init__(self):
        Pagination.__init__(self)

    def setUpConnect(self):
        """
        添加按钮槽函数
        :return:
        """
        self.prevButton.clicked.connect(self.onPrevPage)
        self.nextButton.clicked.connect(self.onNextPage)
        self.switchPageButton.clicked.connect(self.onSwitchPage)

    def initializedModel(self):
        """
        初始化界面数据，待重写
        :return:
        """

        # 测试表格
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可修改
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 选中时选一行
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.horizontalHeader().setFixedHeight(30)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.setRowCount(self.pageRecordCount)
        # self.table.setHorizontalHeaderLabels(['id', u'标题', u'内容', u'操作'])
        # self.table.setColumnHidden(0, True)  # 隐藏某列
        for j in range(20):
            for i in range(5):
                item = QTableWidgetItem(str(i))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(j, i, item)

    def queryRecord(self, limitIndex):
        """
        根据分页查询记录，待重写
        :param limitIndex:开头记录位置
        :return:
        """
        pass

    def onPrevPage(self):
        """
        上一页
        :return:
        """

        self.currentPage -= 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onNextPage(self):
        """
        下一页
        :return:
        """

        self.currentPage += 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onSwitchPage(self):
        """
        切换到指定页面
        :return:
        """

        szText = self.switchPageLineEdit.text()
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(szText)
        if not match:
            QMessageBox.information(self, "提示", "请输入数字.")
            return
        if szText == "":
            QMessageBox.information(self, "提示", "请输入跳转页面.")
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页，清重新输入.")
            return

        limitIndex = (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage = pageIndex
        self.updateStatus()

    def updateStatus(self):
        """
        更新控件状态
        :return:
        """

        self.currentPageLabel.setText(str(self.currentPage))
        self.totalPageLabel.setText(str(self.totalPage))
        if self.currentPage <= 1:
            self.prevButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)

        if self.currentPage >= self.totalPage:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)


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


class Register(RegisterWindow):
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
        # 添加顺序一定按照按钮顺序
        self.right_layout.addWidget(self.ShowNotes(user_id=user_id, user_type=user_type))  # ！？可能存在切换后切回不是初始状态
        self.setUpConnect()

    def setUpConnect(self):
        """
        绑定按钮槽函数
        :return: None
        """

        map(lambda x: x.clicked.connect(self.switchPage), self.bts)

    def switchPage(self):
        """
        点击菜单按钮后切换页面
        :return: None
        """

        # 可能与其他sender冲突
        try:
            index = self.menu_dict[self.sender().objectName()]
            self.right_layout.setCurrentIndex(index)
        except:
            pass

    class ShowNotes(NoteTable):
        """
        继承NoteTable封装业务逻辑
        数据需求：未过期公告序列｜过期公告序列
        描述：【教师】两个表格分别为过期公告和未过期公告表
    　　　    【学生】一个表格未过期公告表
        """

        def __init__(self, user_id, user_type):
            NoteTable.__init__(self)
            if UserType(int(user_type)) is UserType.Teacher:  # 教师
                self.lay.addWidget(self.CurrentNote(), 2, 0, 5, 5)  # 未过期公告表
                self.lay.addWidget(self.PreviousNote(), 2, 5, 5, 5)  # 过期公告表
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)
            elif UserType(int(user_type)) is UserType.Student:  # 学生
                self.lay.addWidget(self.CurrentNote(), 2, 0, 5, 5)
                self.bt_insert.hide()
                self.l_previous_note.hide()
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)

        class CurrentNote(Page):
            """
            未过期的公告表
            """

            def __init__(self):
                Page.__init__(self)

            def queryRecord(self, limitIndex):
                """
                重写查询记录
                :param limitIndex:
                :return:
                """


        class PreviousNote(Page):
            """
            过期的公告表
            """

            def __init__(self):
                Page.__init__(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_ = Management(201610414206, 0)
    win_.show()
    # win1 = SysHome()
    # win2 = MyInfo()
    # win2.show()
    # win3 = Register()
    # win3.show()
    # win4 = Warning()
    # win4.show()
    sys.exit(app.exec_())
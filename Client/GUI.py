# -*-coding:utf-8-*-
import sys
from ui_design.ui_finish import *
from TypesEnum import *
from ClientRequest import CR


class Page(Pagination):
    """
    数据表分页，构建基本事件响应函数
    Management中多个控件需要重写此类
    """

    def __init__(self):
        Pagination.__init__(self)
        # 在继承重写后再执行以下初始化函数

    def setUpConnect(self):
        """
        添加按钮槽函数
        :return:
        """
        self.prevButton.clicked.connect(self.onPrevPage)
        self.nextButton.clicked.connect(self.onNextPage)
        self.switchPageButton.clicked.connect(self.onSwitchPage)
        self.table.clicked.connect(self.showRecord)

    def initializedModel(self):
        """
        初始化界面数据，待重写
        :return:
        """

        pass

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
            # QMessageBox.information(self, "提示", "请输入数字.")
            msg = Warning(words=u"请输入数字")
            msg.exec_()
            return
        if szText == "":
            # QMessageBox.information(self, "提示", "请输入跳转页面.")
            msg = Warning(words=u"请输入跳转页面")
            msg.exec_()
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            # QMessageBox.information(self, "提示", "没有指定的页，清重新输入.")
            msg = Warning(words=u"没有指定的页，清重新输入")
            msg.exec_()
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

    def showRecord(self):
        """
        双击表格显示具体记录信息，待重写
        :return:
        """

        pass

    def addRecords(self, col_list, data):
        """
        添加记录
        :param col_list:[(colname, is_hidden, is_pk), ...]
        :return: None
        """

        self.table.clearContents()  # 清空内容
        self.table.setColumnCount(len(col_list))
        self.table.setRowCount(self.pageRecordCount)
        self.table.setHorizontalHeaderLabels(map(lambda x: x['name'], col_list))  # 设置表头
        map(lambda x: self.table.setColumnHidden(x[0], x[1]['is_hidden']), enumerate(col_list))  # 隐藏某些列
        for num_r, row in enumerate(data):
            pk = []
            self.table.setRowHeight(num_r, 50)
            for num_c, col in enumerate(col_list):
                if col['is_pk']:  # 添加主键
                   pk.append(row[num_c])
                if col['name'] == u'操作':  # 操作栏
                    self.table.setCellWidget(num_r, num_c, self.addOperationButton(pk))
                else:  # 普通字段
                    item = QTableWidgetItem(str(row[num_c]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.table.setItem(num_r, num_c, item)

    def addOperationButton(self, primay_key):
        """
        添加操作按钮，待重写
        :return:
        """
        widget = QWidget()
        bt = OperationButtonInTable(name=u'作废')
        bt.clicked.connect(lambda : self.operationOnBtClicked(primay_key))
        hLayout = QHBoxLayout()
        hLayout.addWidget(bt)
        widget.setLayout(hLayout)
        return widget

    def operationOnBtClicked(self, primary_key):
        """
        操作按钮槽函数，待重写
        :param primary_key:　主键
        :return:
        """
        
        pass

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

    def __init__(self, words=None):
        super(Warning, self).__init__()
        if words:
            self.words.setText(words)
        else:
            pass
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

    # 以下为内部组件类
    class ShowNotes(NoteTable):
        """
        继承NoteTable封装业务逻辑
        数据需求：未过期公告序列｜过期公告序列
        描述：【教师】两个表格分别为过期公告和未过期公告表
    　　　    【学生】一个表格未过期公告表
        """

        def __init__(self, user_id, user_type):
            NoteTable.__init__(self)
            if UserType(int(user_type)) == UserType.Teacher:  # 教师
                self.lay.addWidget(self.CurrentNote(user_type), 2, 0, 5, 5)  # 未过期公告表
                self.lay.addWidget(self.PreviousNote(), 2, 5, 5, 5)  # 过期公告表
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)
            elif UserType(int(user_type)) == UserType.Student:  # 学生
                self.lay.addWidget(self.CurrentNote(user_type), 2, 0, 5, 5)
                self.bt_insert.hide()
                self.l_previous_note.hide()
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)

        class CurrentNote(Page):
            """
            未过期的公告表
            """

            def __init__(self, user_type):
                Page.__init__(self)
                self.col_list = [
                    {'name': 'id', 'is_hidden': True, 'is_pk': True},
                    {'name': u'标题', 'is_hidden': False, 'is_pk': False},
                    {'name': u'内容', 'is_hidden': False, 'is_pk': False},
                    {'name': u'发布日期', 'is_hidden': False, 'is_pk': False},
                    {'name': 'is_valid', 'is_hidden': True, 'is_pk': False},
                ]  # 必须按照数据字段顺序
                if UserType(user_type) == UserType.Teacher:
                    self.col_list.append({'name': u'操作', 'is_hidden': False, 'is_pk': False})
                self.initializedModel()
                self.setUpConnect()
                self.updateStatus()

            def initializedModel(self):
                try:
                    conn = CR()
                    notes = conn.GetAllNotesRequest(0, self.pageRecordCount)['valid']
                    self.totalRecordCount = len(notes)
                    if self.totalRecordCount % self.pageRecordCount == 0:
                        if self.totalRecordCount != 0:
                            self.totalPage = self.totalRecordCount / self.pageRecordCount
                        else:
                            self.totalPage = 1
                    else:
                        self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
                    self.addRecords(self.col_list, notes)
                    conn.CloseChannnel()
                except Exception as e:
                    print(e)
                    warning = Warning(words=u"请求失败！")
                    warning.exec_()

            def queryRecord(self, limitIndex):
                """
                重写查询记录
                :param limitIndex:从第limitIndex条开始
                :return:
                """

                try:
                    conn = CR()
                    notes = conn.GetAllNotesRequest(limitIndex, self.pageRecordCount)
                    self.addRecords(self.col_list, notes['valid'])
                    conn.CloseChannnel()
                except Exception as e:
                    print(e)
                    warning = Warning(words=u"请求失败！")
                    warning.exec_()

        class PreviousNote(Page):
            """
            过期的公告表
            """

            def __init__(self):
                Page.__init__(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_ = Management(201610414206, 1)
    win_.show()
    # win1 = SysHome()
    # win2 = MyInfo()
    # win2.show()
    # win3 = Register()
    # win3.show()
    # win4 = Warning()
    # win4.show()
    sys.exit(app.exec_())
# -*-coding:utf-8-*-
import sys
from ui_design.ui_finish import *
from TypesEnum import *
from ClientRequest import CR
from TableColumnDict import TABLE_COLUMN_DICT


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
        self.table.doubleClicked.connect(self.showRecord)

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
            msg = Alert(words=u"请输入数字")
            msg.exec_()
            return
        if szText == "":
            # QMessageBox.information(self, "提示", "请输入跳转页面.")
            msg = Alert(words=u"请输入跳转页面")
            msg.exec_()
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            # QMessageBox.information(self, "提示", "没有指定的页，清重新输入.")
            msg = Alert(words=u"没有此页")
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

        # self.table.clearContents()  # 清空内容
        map(lambda x: self.table.removeRow(x), range(self.table.rowCount()))
        self.table.setColumnCount(len(col_list))
        # 无需设置固定行数，利用insertRow动态添加
        # self.table.setRowCount(self.pageRecordCount)
        self.table.setHorizontalHeaderLabels(map(lambda x: x['name'], col_list))  # 设置表头
        map(lambda x: self.table.setColumnHidden(x[0], x[1]['is_hidden']), enumerate(col_list))  # 隐藏某些列
        for num_r, row in enumerate(data):
            self.table.insertRow(num_r)
            pk = []
            self.table.setRowHeight(num_r, 50)
            for num_c, col in enumerate(col_list):
                if col['is_pk']:  # 添加主键
                   pk.append(row[num_c])
                if col['name'] == u'操作':  # 操作栏
                    self.table.setCellWidget(num_r, num_c, self.addOperationButton(pk))
                else:  # 普通字段
                    item = QTableWidgetItem(u"{}".format(row[num_c]))  # 注意中文编码
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


class Alert(WarningWindow):
    """
    警告提醒窗
    """

    def __init__(self, words=None, _type=None):
        super(Alert, self).__init__()
        if words:
            self.words.setText(words)
        else:
            pass
        if _type == 'alright':
            self.pix = QPixmap('./ui_design/alright.png').scaled(120, 120)
            self.warning.setPixmap(self.pix)
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
        self.page_one = self.ShowNotes(user_id=user_id, user_type=user_type)

        self.right_layout.addWidget(self.page_one)

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
            self.right_layout.widget(index).initPage()  # 所有组内控件重写一个初始化函数解决了堆叠控件切换后刷新问题
        except Exception as e:
            print(e)
            warning = Alert(words=u"切换失败！")
            warning.exec_()

    # 以下为内部组件类 所有init函数参数都必须统一接收user_id user_type 注意顺序
    class ShowNotes(NoteTable):
        """
        继承NoteTable封装业务逻辑
        数据需求：未过期公告序列｜过期公告序列
        描述：【教师】两个表格分别为过期公告和未过期公告表
    　　　    【学生】一个表格未过期公告表
        """

        __update_previous_note_signal = pyqtSignal()  # 更新过期公告信号

        def __init__(self, user_id, user_type):
            NoteTable.__init__(self)
            self.user_type = user_type
            self.user_id = user_id
            if UserType(user_type) == UserType.Teacher:  # 教师
                self.current_note = self.CurrentNote(user_type, self.__update_previous_note_signal)
                self.lay.addWidget(self.current_note, 2, 0, 5, 5)  # 未过期公告表
                self.previous_note = self.PreviousNote(user_type)
                self.lay.addWidget(self.previous_note, 2, 5, 5, 5)  # 过期公告表
                self.__update_previous_note_signal.connect(lambda :self.updatePreviousNote(self.previous_note))
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)
            elif UserType(user_type) == UserType.Student:  # 学生
                self.current_note = self.CurrentNote(user_type)
                self.lay.addWidget(self.current_note, 2, 0, 5, 5)
                self.bt_insert.hide()
                self.l_previous_note.hide()
                self.lay.setRowStretch(1, 1)
                self.lay.setRowStretch(3, 4)
                self.lay.setRowStretch(7, 1)

        def initPage(self):
            """
            用于切换页面后的初始化页面，仅初始化必要控件
            :return: None
            """

            if UserType(self.user_type) == UserType.Teacher:
                self.previous_note.initializedModel()
                self.previous_note.updateStatus()
            self.current_note.initializedModel()
            self.current_note.updateStatus()


        def updatePreviousNote(self, widget):
            """
            教师作废公告后刷新过期公告栏
            :param widget: 控件对象
            :return: None
            """

            widget.initializedModel()

        class CurrentNote(Page):
            """
            未过期的公告表
            """

            def __init__(self, user_type, update_signal=None):
                Page.__init__(self)
                self.update_signal = update_signal
                self.col_list = TABLE_COLUMN_DICT[UserType(user_type)]['current_note']  # 获取表头信息
                self.initializedModel()
                self.setUpConnect()
                self.updateStatus()

            def initializedModel(self):
                try:
                    conn = CR()
                    self.totalRecordCount = conn.GetCountRequest('note', {'is_valid':NoteStatus.Valid.value})
                    conn.CloseChannnel()
                    if self.totalRecordCount % self.pageRecordCount == 0:
                        if self.totalRecordCount != 0:
                            self.totalPage = self.totalRecordCount / self.pageRecordCount
                        else:
                            self.totalPage = 1
                    else:
                        self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
                    self.queryRecord(0)
                except Exception as e:
                    print(e)
                    warning = Alert(words=u"查询失败！")
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
                    warning = Alert(words=u"查询失败！")
                    warning.exec_()

            def operationOnBtClicked(self, primary_key):
                """
                重写操作按钮
                :param primary_key: 主键
                :return: None
                """

                try:
                    conn = CR()
                    # 更新
                    res = conn.VoidTheNote(primary_key)
                    if res == ClientRequest.Success:
                        alright = Alert(words=u"操作成功！", _type='alright')
                        alright.exec_()
                        self.initializedModel()  # 重新刷新页面
                        self.update_signal.emit()
                    conn.CloseChannnel()
                except Exception as e:
                    print(e)
                    warning = Alert(words=u"操作失败！")
                    warning.exec_()

        class PreviousNote(Page):
            """
            过期的公告表
            """

            def __init__(self, user_type):
                Page.__init__(self)
                self.col_list = TABLE_COLUMN_DICT[UserType(user_type)]['previous_note']  # 获取表头信息
                self.initializedModel()
                self.setUpConnect()
                self.updateStatus()

            def initializedModel(self):
                try:
                    conn = CR()
                    self.totalRecordCount = conn.GetCountRequest('note', {'is_valid':NoteStatus.Invalid.value})
                    conn.CloseChannnel()
                    if self.totalRecordCount % self.pageRecordCount == 0:
                        if self.totalRecordCount != 0:
                            self.totalPage = self.totalRecordCount / self.pageRecordCount
                        else:
                            self.totalPage = 1
                    else:
                        self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
                    self.queryRecord(0)
                except Exception as e:
                    print(e)
                    warning = Alert(words=u"查询失败！")
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
                    self.addRecords(self.col_list, notes['invalid'])
                    conn.CloseChannnel()
                except Exception as e:
                    print(e)
                    warning = Alert(words=u"查询失败！")
                    warning.exec_()



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
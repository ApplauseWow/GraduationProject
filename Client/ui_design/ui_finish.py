# -*-coding:utf-8-*-
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDialog, QLabel, QLCDNumber, QGridLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QEvent
import time

from main_win import Ui_MainWindow
from id_info_win import Ui_id_info_win
from warning_win import Ui_warning_win
from register_win import Ui_register_win


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
        self.buttons = [self.att_rec, self.face_login, self.face_rec, self.face_reg]
        map(lambda x: x.move(desk_width*0.80, desk_height*0.33+self.buttons.index(x)*(x.height()+8)), self.buttons)
        map(lambda x: x.raise_(), self.buttons)

        # 设置时钟
        self.clock = QLCDNumber(self)
        self.clock.setDigitCount(10)
        self.clock.setMode(QLCDNumber.Dec)
        self.clock.setSegmentStyle(QLCDNumber.Flat)
        self.clock.display(time.strftime("%X", time.localtime()))
        self.clock.setStyleSheet("QLCDNumber{color:rgba(255,0,0,100);}")
        self.clock.resize(280, 120)
        self.clock.move(50, desk_height - 30 - self.clock.height())

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
                                      "                   padding:6px; "
                                      "                   text-align: center;                      "
                                      "                   }"),labels)

        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 影藏窗口


class WarningWindow(QDialog, Ui_warning_win):
    """
    识别失败，警告窗口二次设计
    """

    def __init__(self):
        super(WarningWindow, self).__init__()
        self.setupUi(self)

        # 获取桌面尺寸
        desktop = QApplication.desktop()
        desk_width = desktop.availableGeometry().width()
        desk_height = desktop.availableGeometry().height()

        # 窗体定位
        self.move(int(desk_width * 0.3), int(desk_height * 0.3))

        # 设置警告图片和提示语
        self.pix = QPixmap('./ui_design/warning.png').scaled(120, 120)  # 此路径在GUI加载时必须以GUI路径为当前路径，不是此文件
        self.warning.setPixmap(self.pix)
        self.words.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 影藏窗口


class RegisterWindow(QDialog, Ui_register_win):
    """
    人脸注册窗口二次设计
    """

    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)
        self.input_id.installEventFilter(self)

        # 获取桌面尺寸
        desktop = QApplication.desktop()
        desk_width = desktop.screenGeometry().width()
        desk_height = desktop.screenGeometry().height()

        # 移动窗口
        self.move(int(desk_width*0.3), int(desk_height*0.3))

        # 设置按钮样式
        buttons = [self.bt_again, self.bt_cancel, self.bt_reg]
        map(lambda x: x.setStyleSheet("QPushButton{"
"                   background-color:rgba(255,165,0,80);"
"                   border-style:outset;                  "
"                   border-width:4px;                     "
"                   border-radius:10px;                "
"                   border-color:rgba(255,255,255,80);   "
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
"                   }"), buttons)

        # 设置进度条
        self.process.setStyleSheet("QProgressBar "
                                   "{border: 2px solid rgba(255,165,0,255);"
                                   "border-radius: 5px;"
                                   "text-align: center;}"
                                   "QProgressBar::chunk "
                                   "{border: 1px solid rgba(255, 255, 255, 255);"
                                   "border-radius:4px;"
                                   "width: 15px;"
                                   "background:rgba(255,165,0,150);}")
        self.process.setMinimum(0)
        self.process.setMaximum(100)
        self.process.hide()

        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 影藏窗口


class ManageWindow(QDialog):
    """
    资源管理系统界面
    """

    def __init__(self, user_type):
        super(ManageWindow, self).__init__()
        # 界面总体布局控件
        self.whole_layout = QGridLayout()
        self.left_menu = QWidget()
        self.left_layout = QGridLayout()
        self.right_page = QWidget()
        self.right_layout = QGridLayout()
        self.setStyleSheet("background-color: #FF8C00;")
        self.right_page.setStyleSheet('''color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:5px solid darkGray;
        border-right:5px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;''')

        # 左侧菜单按钮
        # --公共组
        self.bt_close = QPushButton(u"退出")
        self.bt_note = QPushButton(u"公告管理" if user_type == 1 else u"查看公告")
        self.bt_group = QPushButton(u"分组管理" if user_type == 1 else u"查看分组")
        self.bt_source = QPushButton(u"资源管理" if user_type == 1 else u"查看资源")
        self.bt_attendance = QPushButton(u"考勤统计")
        self.bt_permit = QPushButton(u"假条审批" if user_type == 1 else u"假条管理")
        self.bt_project = QPushButton(u"项目管理" if user_type == 1 else u"查看项目")
        self.bt_achievement = QPushButton(u"成就管理" if user_type == 1 else u"个人成就")
        self.bt_competition = QPushButton(u"比赛管理" if user_type == 1 else u"参与比赛")
        self.bt_task = QPushButton(u"任务分配" if user_type == 1 else u"查看任务")
        self.bt_seat = QPushButton(u"工委管理" if user_type == 1 else u"查看工位")
        self.bts_pub = [self.bt_note, self.bt_attendance, self.bt_group,
                        self.bt_project,self.bt_competition, self.bt_achievement,
                        self.bt_permit, self.bt_source, self.bt_task,
                        self.bt_seat, self.bt_close]
        # --教师组
        self.bt_t_stuff = QPushButton(u"人事管理")
        self.bts_teacher = [self.bt_t_stuff]
        # --学生组
        self.bt_s_selfInfo = QPushButton(u"个人信息")
        self.bts_stu = [self.bt_s_selfInfo]

        self.init_ui(user_type)

    def init_ui(self, user_type):
        """
        初始化界面
        :param user_type:用户类型 学生０　教师１
        :return: None
        """

        # 界面布局
        self.left_menu.setLayout(self.left_layout)
        self.right_page.setLayout(self.right_layout)

        # 组合按钮
        bts = self.bts_teacher if user_type == 1 else self.bts_stu
        bts.extend(self.bts_pub)

        # 根据按钮个数设置左右布局
        self.whole_layout.addWidget(self.left_menu, 0, 0, len(bts), 2)  # 左部菜单在０行０列开始占１２行３列
        self.whole_layout.addWidget(self.right_page, 0, 2, len(bts), len(bts)-2)  # 右部页面在０行３列开始占１２行１０列

        # 布置按钮
        for row, bt in enumerate(bts):  # 排列按钮
            self.left_layout.addWidget(bt, row, 0, 1, 3)  # 从row行0列开始占1行3列
            bt.setStyleSheet("QPushButton{"
"                   background-color:rgba(255,255,255,255);"
"                   border-style:outset;                  "
"                   border-width:4px;                     "
"                   border-radius:20px;                "
"                   border-color:rgba(255,255,255,255);   "
"                   font:bold 23px;                    "
"                   color:rgba(255,165,0,255);                "
"                   padding:6px;                      "
"                   }"
"                   QPushButton:pressed{"
"                   background-color:rgba(255,165,0,255);"
"                   border-color:rgba(255,255,255,30);"
"                   border-style:inset;"
"                   color:rgba(255,255,255,255);"
"                   }"
"                   QPushButton:hover{"
"                   background-color:rgba(255,165,0,255);"
"                   border-color:rgba(255,255,255,255);"
"                   color:rgba(255,255,255,255);"
"                   }")

        self.setLayout(self.whole_layout)

        self.setWindowFlags(Qt.FramelessWindowHint)  # 影藏窗口
        self.showFullScreen()


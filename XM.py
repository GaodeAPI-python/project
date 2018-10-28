
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from pymysql import connect
from PyQt5.QtWebEngineWidgets import *
from youxiang import userinfo
import hashlib

from hashlib import sha1

# app.exec_()其实就是QApplication的方法，
# 原来这个exec_()方法的作用是“进入程序的主循环直到exit()被调用

#--
name = 0
pwd = 0
#--


class Main_window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('仿宋', 10))

        self.setToolTip('')

        #背景
        label = QLabel('',self)
        self.gif = QMovie('water6.gif')
        label.setMovie(self.gif)
        self.gif.start()

        #标题
        biaoti = QLabel('高德API在线租房',self)
        biaoti.setFont(QFont('宋体', 28))
        biaoti.resize(290,170)
        # biaoti.move(362,0)
        biaoti.move(352,0)
        biaoti.setStyleSheet('QLabel{color:white}'
                             'QLabel:hover{color:gold}')

        #登录按钮并设置鼠标悬停提示
        login = QPushButton('登录', self)
        login.setToolTip('点击登录')
        #调整按钮尺寸为默认宽高
        # login.resize(login.sizeHint())
        #设置按钮在窗口中位置距左500距上0
        login.move(420, 250)
        login.resize(86,32)
        #设置按钮背景图
        login.setStyleSheet('QPushButton{background-image:url(blue5.png)}'
                            'QPushButton:hover{background-image:url(blue5_2.png)}'
                            'QPushButton{color:white}')
        login.setFlat(True)
        #窗口和控件都半透明
        # login.setWindowOpacity(0.1)
        

        # self.register = QPushButton('注册')
        #注册按钮并设置鼠标悬停提示
        register = QPushButton('注册', self)
        register.setToolTip('点击注册')
        register.move(515, 250)
        register.resize(86,32)
        register.setStyleSheet('QPushButton{background-image:url(blue5.png)}'
                               'QPushButton:hover{background-image:url(blue5_2.png)}'
                               'QPushButton{color:white}')
        register.setFlat(True)


        # 设置按钮事件
        #设置注册按钮跳转
        register.clicked.connect(self.pushButton1_clicked1)
        #设置登录按钮事件
        login.clicked.connect(self.pushButton2_clicked2)

        #帐号
        name = QLabel('帐号:',self)
        # name.setFont(QFont('宋体'))
        name.move(370,150)
        name.setStyleSheet('QLabel{color:white}')

        #帐号输入框
        name_text = QLineEdit(self)
        name_text.resize(180,30)
        name_text.move(420,143)

        #密码
        passwd = QLabel('密码:',self)
        # passwd.setFont(QFont('宋体'))
        passwd.move(370,200)
        passwd.setStyleSheet('QLabel{color:white}')

        #密码输入框
        passwd_text = QLineEdit(self)
        passwd_text.installEventFilter(self)
        passwd_text.resize(180,30)
        passwd_text.move(420,195)
        passwd_text.setContextMenuPolicy(Qt.NoContextMenu)
        passwd_text.setPlaceholderText('只包含数字和字母')
        passwd_text.setEchoMode(QLineEdit.Password)

        #创建一个关闭按钮
        quit = QPushButton('x',self)
        quit.clicked.connect(QCoreApplication.instance().quit)
        quit.resize(18,18)
        quit.move(0,0)
        quit.setToolTip('点击关闭')
        quit.setFlat(True)
        quit.setStyleSheet('QPushButton{background-color:white}'
                           'QPushButton{color:black}'
                           'QPushButton:hover{color:gold}')

        # 设置窗口离左边的距离50 上面的距离100 宽800，高500
        # self.setGeometry(600, 350, 658, 500)
#--
        self.resize(658,380)
        self.center()
#--

        # 设置title
        self.setWindowTitle('高德API租房')
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.name_text = name_text
        self.passwd_text = passwd_text

    def center(self):
        #计算出显示器的分辨率相当于screen.width() * screen.height()
        screen = QDesktopWidget().screenGeometry()

        #该语句用来获取QWidget窗口的大小相当于size.width()* size.heiget()
        size = self.geometry()

        #将窗口移动到屏幕正中央
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    windowList = []
    def pushButton1_clicked1(self):
        the_window = SecondWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    windowList = []
    def pushButton2_clicked2(self):
#--
        global name
        global pwd
#--
        name = self.name_text.text()
        pwd = self.passwd_text.text()


        if name=='' or pwd=='':
#--         
            # cb = QCheckBox('所有文档都按此操作')
            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('警告')
            # msgBox.setIcon(QMessageBox.warning)
            # msgBox.setText('这是一个警告消息对话框')

            # Yes = msgBox.addButton('是的',QMessageBox.YesRole)
            # msgBox.setDefaultButton(Yes)
            # msgBox.setCheckBox(cb)
            # cb.stateChanged.connect(self.check)
            # msgBox.exec()

            # cb = QCheckBox('所有文档都按此操作')
            # cb = QCheckBox()
#--
            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('警告')
            # msgBox.setIcon(QMessageBox.Warning)
            # msgBox.setText('账户名，密码不能为空')
#--
            # msgBox.setInformativeText('出现更改愿意保存吗?')
#--
            # Ok = msgBox.addButton('好的', QMessageBox.AcceptRole)
#--
            # NoSave = msgBox.addButton('取消', QMessageBox.RejectRole)
            # Cancel = msgBox.addButton('不保存', QMessageBox.DestructiveRole)
            # msgBox.setDefaultButton(Ok)
            # msgBox.setCheckBox(cb)
            # cb.stateChanged.connect(self.check)
#--
            # reply = msgBox.exec()
            # reply = QMessageBox.AcceptRole
#--
            #     self.la.setText('你选择了保存！')
            # elif reply == QMessageBox.RejectRole:
            #     self.la.setText('你选择了取消！')
            # else:
            #     self.la.setText('你选择了不保存！')

#--            
            print(QMessageBox.warning(self,'警告','表单不能为空',QMessageBox.Yes,QMessageBox.Yes))
            return
        else:
#--
            # m = hashlib.md5()
            # m.update(pwd.encode())

            # sha1加密
            m = sha1()
            m.update(pwd.encode('utf-8'))

#--
            db = connect(host='localhost',
                         user='root',
                         password='123456',
                         database='study',
                         charset='utf8',
                         port=3306)

            cursor = db.cursor()
            sql = "select name,pwd from userinfo where name=%s and pwd=%s;"
            # cursor.execute(sql,[name,pwd])

            cursor.execute(sql,[name,m.hexdigest()])
            result=cursor.fetchall()
            if len(result)==0:
                print(QMessageBox.warning(self,'请重新输入','账户名或密码错误!',QMessageBox.Yes,QMessageBox.Yes))
                # msgBox = QMessageBox()
                # msgBox.setWindowTitle('警告')
                # msgBox.setIcon(QMessageBox.Warning)
                # msgBox.setText('账户名或密码错误')
                # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
                # # msgBox.setDefaultButton(Ok)
                # msgBox.exec()
                # QMessageBox.AcceptRole
                return
            else:
                # Welcome = WelcomeWindow()
                Welcome = WelcomeWindow1()
                self.windowList.append(Welcome)
                self.close()
                Welcome.show()
            
            cursor.close()
            db.close()

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('高德API租房系统欢迎您！')
        
        self.setGeometry(650,100,1263,640)

        self.setWindowFlags(Qt.FramelessWindowHint)
        # 窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        #背景
        label = QLabel('',self)
        self.gif = QMovie('rain.gif')
        label.setMovie(self.gif)
        self.gif.start()

        #昵称
        nickname = QLabel('欢迎您！%s'%name,self)
        nickname.setFont(QFont('宋体'))
        nickname.move(1000,10)
        nickname.setStyleSheet('QLabel{color:black}')

        #注销
        logout = QLabel('按ESC注销',self)
        logout.setFont(QFont('宋体'))
        logout.move(1116,10)
        logout.setStyleSheet('QLabel{color:black}')
        # logout.setFlat(True)

        # self.browser = QWebEnginerView()
        # self.browser.load(QUrl('http://www.baidu.com'))
        # self.setCentrawWidget(self.browser)

#--
        #设置点击注销回到登录界面
        # logout.clicked.connect()
#--
        #收藏
        collection = QPushButton('收藏',self)
        collection.setFont(QFont('宋体'))
        collection.move(1180,5)
        collection.setStyleSheet('QLabel{color:black}')
        collection.setFlat(True)

        #创建一个关闭按钮
        quit = QPushButton('X',self)
        quit.clicked.connect(QCoreApplication.instance().quit)
        quit.resize(42,42)
        quit.move(0,0)
        quit.setToolTip('点击关闭')
        quit.setFlat(True)
        quit.setStyleSheet('QPushButton{background-color:white}'
                           'QPushButton{color:white}'
                           'QPushButton:hover{color:black}')
        
        # view = QWebEnginerView()
        # view.load(Qurl.fromLocalFile('/home/tarena/zsh/PyQt/xm1.5/main1.html'))


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
#--
    #按esc退出登录
    windowList = []
    def keyPressEvent(self, e):
        the_window = Main_window()
        self.windowList.append(the_window)
        
        if e.key() == Qt.Key_Escape:
            the_window.show()
            self.close()


    # windowList = []
    # def question(self):
    #     the_window = Main_window()
    #     value = QMessageBox.warning(self,'高德API在线租房','您确定返回登录界面吗？',QMessageBox.Yes,QMessageBox.No)
    #     if value == QMessageBox.Yes:
            
    #         WelcomeWindow.close()
    #         the_window.show()



    # windowList = []
    # def closeEvent(self, event):
    #     # QMessageBox.question(self,'高德API在线租房','是否要退出注册',QMessageBox.Yes,QMessageBox.Yes)
    #     the_window = Main_window()
    #     self.windowList.append(the_window)
    #     the_window.show()
    #     event.accept()
#--

#Web窗口
class WelcomeWindow1(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('高德API在线租房')
        self.setWindowIcon(QIcon('icons/icon.png'))

        # self.setGeometry(350,200,1263,640)
#--
        self.resize(1263,640)
        self.center()
#--

        # 设置窗口无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
     
        self.browser = QWebEngineView()
        url = '/home/tarena/zsh/PyQt/xm1.75/map01.html'
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)
        self.statusBar().showMessage("当前用户：%s"%name)
        #创建一个菜单栏
        menubar = self.menuBar()
        #为了全平台统一显示
        menubar.setNativeMenuBar(False)
        #在菜单栏中添加一个菜单
        fileMenu = menubar.addMenu('我的')
        
        #给菜单添加一个注销功能
        logout = QAction(QIcon('exit.png'), '注销', self)
        #给注销按钮设置快捷键
        logout.setShortcut('ESC')
        #鼠标悬停到注销按钮上提示：退出登录
        logout.setStatusTip('退出登录')
        # exitAction.triggered.connect(qApp.quit)
        logout.triggered.connect(self.question)

        #给菜单添加收藏功能
        collection = QAction('收藏',self)
        collection.setStatusTip('添加到收藏夹')
#--
        #给菜单添加合同功能
        agreement = QAction('合同',self)
        agreement.setStatusTip('添加到收藏夹')

        #给菜单添加账单功能
        bill = QAction('账单',self)
        bill.setStatusTip('添加到收藏夹')

        #给菜单添加约看功能
        atsee = QAction('约看',self)
        atsee.setStatusTip('添加到收藏夹')

        #给菜单添加管家功能
        steward = QAction('管家',self)
        steward.setStatusTip('添加到收藏夹')
#--
        #将注销功能添加到菜单中
        fileMenu.addAction(logout)
        #将收藏功能添加到菜单中
        fileMenu.addAction(collection)
#--
        #将合同功能添加到菜单中
        fileMenu.addAction(agreement)
        #将账单功能添加到菜单中
        fileMenu.addAction(bill)
        #将约看功能添加到菜单中
        fileMenu.addAction(atsee)
        #将管家功能添加到菜单中
        fileMenu.addAction(steward)

#--

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
#--
    #合同界面
    windowList=[]
    def on_agreement(self):
        the_window = Main_window()
        self.windowList.append(the_window)#打开合同主界面

        #与服务端交互
        def do_hetong(s,id):
            msg = 'H {}'.format(id)
            s.send(msg.encode())
            data = s.recv(128).decode() 
            if data == 'OK':
                while True:
                    data = s.recv(1024).decode()
                    if data == '##':
                        break
                    print(data)
            else:
                print("您还未签合同")

    #账单界面
    windowList=[]
    def on_bill(self):
        the_window = Main_window()
        self.windowList.append(the_window)

        def do_zhangdan(s,id):
            msg = 'Z {}'.format(id)
            s.send(msg.encode())
            data = s.recv(128).decode() 
            if data == 'OK':
                while True:
                    data = s.recv(1024).decode()
                    if data == '##':
                        break
                    print(data)
            else:
                print("您暂时没有账单")

    #约看界面   
    windowList=[]
    def on_atsee(self):
        the_window = Main_window()
        self.windowList.append(the_window)

        def do_yuekan(s,id):
            msg = 'Y {}'.format(id)
            s.send(msg.encode())
            data = s.recv(128).decode() 
            if data == 'OK':
                while True:
                    data = s.recv(1024).decode()
                    if data == '##':
                        break
                    print(data)
            else:
                print("您暂时没有约看")

    #管家界面
    windowList=[]
    def on_steward(self):
        the_window = Main_window()
        self.windowList.append(the_window)
        def do_guanjia(s,id):
            msg = 'G {}'.format(id)
            s.send(msg.encode())
            data = s.recv(128).decode() 
            if data == 'OK':
                print('您好，***为您服务')
                while True:
                    data = input('发送....')
                    if not data:
                        break
                    s.send(data.encode())
                    data = s.recv(1024)
                    print('接收到',data.decode())
#--
    #注销
    windowList=[]
    def question(self):
        the_window = Main_window()
        self.windowList.append(the_window)
        regex = QMessageBox.warning(self,'高德API在线租房','确定要退出登录吗？',QMessageBox.Yes,QMessageBox.No)
        if regex == QMessageBox.Yes:
            the_window.show()
            self.close()
        else:
            pass

    # windowList1 = []
    # def closeEvent(self, event):
    #     # QMessageBox.question(self,'高德API在线租房','是否要退出注册',QMessageBox.Yes,QMessageBox.Yes)
    #     the_window = Main_window()
    #     self.windowList1.append(the_window)
    #     the_window.show()
    #     event.accept()

    # def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
    #     self._endPos = e.pos() - self._startPos
    #     self.move(self.pos() + self._endPos)

    # def mousePressEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = True
    #         self._startPos = QPoint(e.x(), e.y())

    # def mouseReleaseEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = False
    #         self._startPos = None
    #         self._endPos = None


    # #按esc退出登录
    # windowList = []
    # def keyPressEvent(self, e):
    #     the_window = Main_window()
    #     self.windowList.append(the_window)
        
    #     if e.key() == Qt.Key_Escape:
    #         the_window.show()
    #         self.close()



class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('注册界面')
        
        # self.setGeometry(700,200,500,717)
#--
        self.resize(500,717)
        self.center()

#--
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        # 窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        #背景
        label = QLabel('',self)
        self.gif = QMovie('fire.gif')
        label.setMovie(self.gif)
        self.gif.start()

        #设置窗口布局
        #帐号输入框
        self.register_name_text = QLineEdit(self)
        self.register_name_text.resize(200, 30)
        self.register_name_text.move(20,100)

        #帐号要求
        self.register_name_yq = QLabel('* 昵称',self)
        self.register_name_yq.move(235,102)
        self.register_name_yq.setStyleSheet('QLabel{color:white}' 'QLabel{font-family:"华文新魏"}')

        #密码输入框
        self.register_pwd_text = QLineEdit(self)
        self.register_pwd_text.resize(200,30)
        self.register_pwd_text.move(20,170)
        #给密码框安装事件过滤器
        self.register_pwd_text.installEventFilter(self)
        #设置密码框无法复制
        self.register_pwd_text.setContextMenuPolicy(Qt.NoContextMenu)
        #设置密码框显示样式
        self.register_pwd_text.setEchoMode(QLineEdit.Password)

        #密码要求
        self.register_pwd_yq = QLabel('* 密码：开头为大写字母，不超过16位',self)
        self.register_pwd_yq.move(235,172)
        self.register_pwd_yq.setStyleSheet('QLabel{color:white}' 'QLabel{font-family:"华文新魏"}')


        self.register_pwd_yq2 = QLabel('（只包含字母和数字）',self)
        self.register_pwd_yq2.move(280,192)
        self.register_pwd_yq2.setStyleSheet('QLabel{color:white}' 'QLabel{font-family:"华文新魏"}')

        #密码输入框2
        self.register_pwd2_text = QLineEdit(self)
        self.register_pwd2_text.resize(200,30)
        self.register_pwd2_text.move(20,240)
        #设置密码框无法复制
        self.register_pwd2_text.setContextMenuPolicy(Qt.NoContextMenu)
        #设置密码框显示样式
        self.register_pwd2_text.setEchoMode(QLineEdit.Password)

        #密码2要求
        self.register_pwd_yq = QLabel('* 请再次输入密码',self)
        self.register_pwd_yq.move(235,242)
        self.register_pwd_yq.setStyleSheet('QLabel{color:white}' 'QLabel{font-family:"华文新魏"}')

        #邮箱输入框
        self.register_email_text = QLineEdit(self)
        self.register_email_text.resize(200,30)
        self.register_email_text.move(20,310)
        self.register_email_text.installEventFilter(self)

        #邮箱要求
        self.register_email_yq = QLabel('* 邮箱验证，请填写邮箱地址',self)
        self.register_email_yq.move(235,312)
        self.register_email_yq.setStyleSheet('QLabel{color:white}' 'QLabel{font-family:"华文新魏"}')

        #验证码输入框
        self.register_verification_text = QLineEdit(self)
        self.register_verification_text.resize(100,30)
        self.register_verification_text.move(20,380)

        #点击获取验证码
        self.register_verification_btn = QPushButton(' 获取验证码',self)
        self.register_verification_btn.resize(90,30)
        self.register_verification_btn.move(130,380)
        self.register_verification_btn.setFlat(True)
        self.register_verification_btn.setStyleSheet('QPushButton{font-size:12px}'
                                                     'QPushButton{font-family:"华文新魏"}'
                                                     'QPushButton{color:gold}'
                                                     'QPushButton:hover{color:orange}'
                                                     'QPushButton{background-image:url(check1.png)}'
                                                     'QPushButton:hover{background-image:url(check2.png)}')

        #验证码要求
        self.register_verification_yq = QLabel('* 点击发送验证码到邮箱',self)
        self.register_verification_yq.move(235,382)
        self.register_verification_yq.setStyleSheet('QLabel{color:white}')

        #注册大按钮
        self.register_big = QPushButton('注  册',self)
        self.register_big.resize(100,100)
        self.register_big.move(350,580)
        self.register_big.setFlat(True)
        self.register_big.setStyleSheet('QPushButton{border-radius:50px}'
                                        'QPushButton{background-image:url(register_1.png)}'
                                        'QPushButton:hover{background-image:url(register_3.png)}')

        # #创建一个关闭按钮
        # quit = QPushButton('x',self)
        # # quit.clicked.connect(self.closeEvent)
        # quit.clicked.connect(QCoreApplication.instance().quit)
        # quit.resize(18,18)
        # quit.move(0,0)
        # quit.setToolTip('点击关闭')
        # quit.setFlat(True)
        # quit.setStyleSheet('QPushButton{background-color:white}'
        #                    'QPushButton{color:black}'
        #                    'QPushButton:hover{color:gold}')
#--
        # 密码框过滤
        reg = QRegExp('^[A-Z]{1}[A-Za-z|_|0-9]{5,16}$')
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.register_pwd_text.setValidator(pValidator)
        self.register_pwd2_text.setValidator(pValidator)
        self.register_big.clicked.connect(self.YanZheng)
        self.register_verification_btn.clicked.connect(self.sunc)#获取验证码方法
        self.register_name_text.returnPressed.connect(self.YanZheng)
        self.register_pwd_text.returnPressed.connect(self.YanZheng)
        self.register_pwd2_text.returnPressed.connect(self.YanZheng)

        #邮箱框过滤
        # reg_email = QRegExp('^[\w.-]+@{1}[A-Za-z0-9-]+\.*[A-Za-z0-9-]+\.{1}[A-Za-z]{2,8}$')
        reg_email = QRegExp('^[\w.-]+@{1}[A-Za-z\d-]+\.*[A-Za-z\d-]+\.{1}[A-Za-z]{2,8}$')
        pValidator_email = QRegExpValidator(self)
        pValidator_email.setRegExp(reg_email)
        self.register_email_text.setValidator(pValidator_email)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def sunc(self):
        name=self.register_name_text.text()
        email=self.register_email_text.text()
        # userinfo1=userinfo(name,email)
        # self.code = userinfo1.getcode()

       

#--
        if email == '':
            print(QMessageBox.warning(self,'高德API在线租房系统','请填写邮箱地址',QMessageBox.Ok,QMessageBox.Ok))

            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('高德API在线租房系统')
            # msgBox.setIcon(QMessageBox.Warning)
            # msgBox.setText('请填写邮箱地址')
            # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
            # msgBox.setDefaultButton(Ok)
            # msgBox.exec()
            # QMessageBox.AcceptRole


#--
#         elif not self.code: #如果没有验证码，报错
# #--         
#             print('1')
#             del userinfo1
#             print('2')
#             print(QMessageBox.warning(self,'高德API在线租房系统','验证码不能为空',QMessageBox.Ok,QMessageBox.Ok))
        elif name == '':
            print(QMessageBox.warning(self,'高德API在线租房系统','请填写昵称',QMessageBox.Ok,QMessageBox.Ok))

            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('高德API在线租房系统')
            # msgBox.setIcon(QMessageBox.Warning)
            # msgBox.setText('请填写昵称')
            # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
            # msgBox.setDefaultButton(Ok)
            # msgBox.exec()
            # QMessageBox.AcceptRole
        else:
            userinfo1=userinfo(name,email)
            self.code = userinfo1.getcode()
#--

    def YanZheng(self):
        
        register_name = self.register_name_text.text() 
        register_pwd = self.register_pwd_text.text()
        register_pwd2 = self.register_pwd2_text.text()
        register_email = self.register_email_text.text()
        register_verification = self.register_verification_text.text()

        if register_name == '' or register_pwd == '' or register_pwd2 == '' or register_email == '' or register_verification == '':
            print(QMessageBox.warning(self,'警告','表单不能为空', QMessageBox.Yes, QMessageBox.Yes))
            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('警告')
            # msgBox.setIcon(QMessageBox.Warning)
            # msgBox.setText('表单不能为空')
            # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
            # msgBox.setDefaultButton(Ok)
            # msgBox.exec()
            # QMessageBox.AcceptRole
            return
        elif register_pwd != register_pwd2:
            print(QMessageBox.warning(self,'警告','密码两次输入不一致，请重新输入', QMessageBox.Yes, QMessageBox.Yes))
            # msgBox = QMessageBox()
            # msgBox.setWindowTitle('警告')
            # msgBox.setIcon(QMessageBox.Warning)
            # msgBox.setText('密码两次输入不一致，请重新输入')
            # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
            # msgBox.setDefaultButton(Ok)
            # msgBox.exec()
            # QMessageBox.AcceptRole
            return
        else:
            db = connect(host='localhost',
                         user='root',
                         password='123456',
                         database='study',
                         charset='utf8',
                         port=3306)

            cursor = db.cursor()
            sql = 'select name from userinfo where name=%s;'
            cursor.execute(sql,[register_name])
            # cursor.execute(sql)
            result = cursor.fetchall()
            print('第256行register_name为:',register_name)
            print('第257行result为:',result)
            # A=cursor.execute("select name,pwd from userinfo where name=%s and pwd=%s;"%(register_name,register_pwd))
            if len(result) == 0:
                ###############
                code_text = self.register_verification_text.text()#获取文本框里面的验证码　
                if code_text == self.code:#如果获取的验证码和数据库里面的一样
                    print(code_text,self.code)
                    sql_insert = "insert into userinfo (name,pwd,mail) values(%s,%s,%s);"
                    cursor.execute(sql_insert,[register_name,self.md5(register_pwd),register_email])
                    db.commit()
                    # print(QMessageBox.warning(self,'恭喜','注册成功',QMessageBox.Ok,QMessageBox.Ok))
                    regex = QMessageBox.warning(self,'恭喜！','注册成功！',QMessageBox.Ok,QMessageBox.Ok)
                    if regex == QMessageBox.Ok:
                        self.close()
                    else:
                        pass
                    return
                else:
                    self.register_verification_text.setText('')
                    print(QMessageBox.warning(self,'高德API在线租房系统','验证码不正确请重新输入',QMessageBox.Ok,QMessageBox.Ok))#验证码不一样
                    # msgBox = QMessageBox()
                    # msgBox.setWindowTitle('警告')
                    # msgBox.setIcon(QMessageBox.Warning)
                    # msgBox.setText('验证码不正确请重新输入')
                    # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
                    # msgBox.setDefaultButton(Ok)
                    # msgBox.exec()
                    # QMessageBox.AcceptRole

            elif result[0][0] == register_name:
                print(QMessageBox.warning(self,'警告','用户名被占用',QMessageBox.Yes,QMessageBox.Yes))
                # msgBox = QMessageBox()
                # msgBox.setWindowTitle('警告')
                # msgBox.setIcon(QMessageBox.Warning)
                # msgBox.setText('用户名被占用')
                # Ok = msgBox.addButton('好的',QMessageBox.AcceptRole)
                # msgBox.setDefaultButton(Ok)
                # msgBox.exec()
                # QMessageBox.AcceptRole
                return
            cursor.close()
            db.close()
            return

    def md5(self,pwd):#密码MD5加密        
        # m= hashlib.md5()  #创建md5对象
        # m.update(pwd.encode()) #生成加密串，其中password是要加密的字符串

        m = sha1()
        m.update(pwd.encode('utf-8'))
        return m.hexdigest()  #打印经过md5加密的字符串


#--
    # 重写关闭事件，注册窗口关闭返回主窗口
    windowList = []
    def closeEvent(self, event):
        # QMessageBox.question(self,'高德API在线租房','是否要退出注册',QMessageBox.Yes,QMessageBox.Yes)
        the_window = Main_window()
        self.windowList.append(the_window)
        the_window.show()
        event.accept()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    M = Main_window()
    M.show()
    sys.exit(app.exec_())

        

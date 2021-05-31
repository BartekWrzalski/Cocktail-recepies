# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets
from py.User import sign_in, register, LoginException
from main_app import MainApp


class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.setEnabled(True)
        self.resize(320, 180)
        self.setMouseTracking(False)
        # self.setStyleSheet("background-color: rgb(198, 140, 83)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 111))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label_login = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_login.setFont(font)
        self.horizontalLayout.addWidget(self.label_login)
        spacerItem = QtWidgets.QSpacerItem(46, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.entry_login = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.entry_login.setFont(font)
        # self.entry_login.setStyleSheet("background-color: rgb(217, 179, 140)")
        self.horizontalLayout.addWidget(self.entry_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.horizontalLayout_2.addWidget(self.label_password)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.entry_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.entry_password.setFont(font)
        # self.entry_password.setStyleSheet("background-color: rgb(217, 179, 140)")
        self.horizontalLayout_2.addWidget(self.entry_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 130, 191, 26))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_sign_in = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_sign_in.clicked.connect(self.try_sign_in)
        # self.button_log_out.setStyleSheet("background-color: rgb(217, 179, 140)")
        self.horizontalLayout_3.addWidget(self.button_sign_in)
        self.button_new_account = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_new_account.clicked.connect(self.try_register)
        # self.button_new_account.setStyleSheet("background-color: rgb(217, 179, 140);")
        self.horizontalLayout_3.addWidget(self.button_new_account)
        self.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Sign in"))
        self.label_login.setText(_translate("self", "Login"))
        self.label_password.setText(_translate("self", "Password"))
        self.button_sign_in.setText(_translate("self", "Sign in"))
        self.button_new_account.setText(_translate("self", "Create account"))

    def try_sign_in(self):
        if self.entry_login.text() and self.entry_password.text():
            try:
                sign_in(self.entry_login.text(), self.entry_password.text())
                self.hide()
                if not hasattr(self, 'main_app'):
                    self.main_app = MainApp(self)
                self.main_app.show_popular()
                self.main_app.show()
            except LoginException as e:
                self.statusBar.showMessage(str(e), 1500)
        else:
            self.statusBar.showMessage("Login or password not provided", 1500)

    def try_register(self):
        if self.entry_login.text() and self.entry_password.text():
            try:
                register(self.entry_login.text(), self.entry_password.text())
                self.hide()
                if not hasattr(self, 'main_app'):
                    self.main_app = MainApp(self)
                self.main_app.show_popular()
                self.main_app.show()
            except LoginException as e:
                self.statusBar.showMessage(str(e), 1500)
        else:
            self.statusBar.showMessage("Login or password not provided", 1500)

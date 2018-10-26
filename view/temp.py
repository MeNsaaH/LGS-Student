# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Display(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 658)
        MainWindow.setStyleSheet("QMainWindow , QWidget{\n"
"    background-color: rgb(0, 170, 255);\n"
"    background-color: rgb(35, 134, 255);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    \n"
"    font: 12pt \"Menlo\";\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid #ffffff;\n"
"    height: 2.0em;\n"
"    font: 10pt \"Monaco\";\n"
"    padding: 3px;\n"
"    \n"
"    background-color: rgb(239, 239, 239)\n"
"    }\n"
"QLineEdit:hover{\n"
"    border: 2px solid #ffffff;\n"
"    background-color: rgb(255, 92, 95);\n"
"    height: 2.5em;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgba(255, 148, 148, 234);\n"
"    border: 1px solid #000000;\n"
"}\n"
"QComboBox {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(67, 148, 103);\n"
"    height: 2.0em;\n"
"    font: 10pt \"Menlo\";\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    height:2.0em;\n"
"    font: 10pt \"Consolas\";\n"
"    border-radius: 3px;\n"
"    border: 2px solid rgb(13, 13, 13);\n"
"}\n"
"QPushButton:hover{\n"
"        \n"
"    background-color:rgb(18, 18, 18);\n"
"    color: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setGeometry(QRect(10, 10, 31, 21))
        self.menuBtn.setStyleSheet("#menuBtn{\n"
            "background-color: rgb(35, 134, 255);\n"
            "border: None\n"
            "}\n"
            "\n"
            "#menuBtn:hover{\n"
            "    border: 1px solid #000000;\n"
            "    background: #ffffff;\n"
            "    padding: 3px\n"
            "}"
        )
        self.menuBtn.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/menu"), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(40, 19))
        self.menuBtn.setObjectName("menuBtn")
        self.menuBtn.raise_()
        self.menuBtn.show()

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_26 = QVBoxLayout(self.page)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_13 = QLabel(self.page)
        self.label_13.setText("")
        self.label_13.setPixmap(QPixmap(":/futminna"))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_26.addWidget(self.label_13)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem)
        self.label_17 = QLabel(self.page)
        self.label_17.setStyleSheet("color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"background-color: rgb(231, 231, 231);\n"
"padding: 3px;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_26.addWidget(self.label_17)
        self.label_18 = QLabel(self.page)
        self.label_18.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-style: italic;\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.244318 rgba(255, 255, 0, 69), stop:0.386364 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 69));\n"
"border-radius:0px;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_26.addWidget(self.label_18)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem1)
        self.goto_regBtn = QPushButton(self.page)
        self.goto_regBtn.setObjectName("goto_regBtn")
        self.verticalLayout_26.addWidget(self.goto_regBtn)
        self.goto_loginBtn = QPushButton(self.page)
        self.goto_loginBtn.setObjectName("goto_loginBtn")
        self.verticalLayout_26.addWidget(self.goto_loginBtn)
        self.forgotPassBtn = QPushButton(self.page)
        self.forgotPassBtn.setObjectName("forgotPassBtn")
        self.verticalLayout_26.addWidget(self.forgotPassBtn)
        self.stackedWidget.addWidget(self.page)
        self.registerPage = QWidget()
        self.registerPage.setObjectName("registerPage")
        self.verticalLayout_190 = QVBoxLayout(self.registerPage)
        self.verticalLayout_190.setObjectName("verticalLayout_190")
        self.frame = QFrame(self.registerPage)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Icon = QLabel(self.frame)
        self.Icon.setMaximumSize(QSize(120, 81))
        self.Icon.setText("")
        self.Icon.setPixmap(QPixmap(":/logo/futminna2.png"))
        self.Icon.setAlignment(Qt.AlignCenter)
        self.Icon.setObjectName("Icon")
        self.horizontalLayout.addWidget(self.Icon)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QLabel(self.frame)
        self.label.setStyleSheet("color:rgb(75, 75, 75);\n"
"font: 16pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QFrame(self.frame)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.UsernameLabel = QLabel(self.frame)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.verticalLayout_3.addWidget(self.UsernameLabel)
        self.usernameLineEdit = QLineEdit(self.frame)
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.verticalLayout_3.addWidget(self.usernameLineEdit)
        self.emailLabel = QLabel(self.frame)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout_3.addWidget(self.emailLabel)
        self.emailEdit = QLineEdit(self.frame)
        self.emailEdit.setObjectName("emailEdit")
        self.verticalLayout_3.addWidget(self.emailEdit)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.passwordLabel = QLabel(self.frame)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_3.addWidget(self.passwordLabel)
        self.passwordEdit = QLineEdit(self.frame)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_3.addWidget(self.passwordEdit)
        self.confirmPLabel = QLabel(self.frame)
        self.confirmPLabel.setObjectName("confirmPLabel")
        self.verticalLayout_3.addWidget(self.confirmPLabel)
        self.confirmPLabel_2 = QLineEdit(self.frame)
        self.confirmPLabel_2.setObjectName("confirmPLabel_2")
        self.verticalLayout_3.addWidget(self.confirmPLabel_2)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.regBtn = QPushButton(self.frame)
        self.regBtn.setObjectName("regBtn")
        self.verticalLayout_3.addWidget(self.regBtn)
        self.loginReqBtn = QPushButton(self.frame)
        self.loginReqBtn.setObjectName("loginReqBtn")
        self.verticalLayout_3.addWidget(self.loginReqBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_190.addWidget(self.frame)
        self.stackedWidget.addWidget(self.registerPage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName("loginPage")
        self.verticalLayout_6 = QVBoxLayout(self.loginPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QFrame(self.loginPage)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.Icon_2 = QLabel(self.frame_2)
        self.Icon_2.setMaximumSize(QSize(120, 81))
        self.Icon_2.setText("")
        self.Icon_2.setPixmap(QPixmap(":/futminna_logo"))
        self.Icon_2.setAlignment(Qt.AlignCenter)
        self.Icon_2.setObjectName("Icon_2")
        self.horizontalLayout_2.addWidget(self.Icon_2)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setStyleSheet("color:rgb(75, 75, 75);\n"
"font: 16pt \"Comic Sans MS\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.line_2 = QFrame(self.frame_2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.UsernameLabel_2 = QLabel(self.frame_2)
        self.UsernameLabel_2.setObjectName("UsernameLabel_2")
        self.verticalLayout_5.addWidget(self.UsernameLabel_2)
        self.UsernameLineEdit = QLineEdit(self.frame_2)
        self.UsernameLineEdit.setText("")
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.verticalLayout_5.addWidget(self.UsernameLineEdit)
        self.passwordLabel_2 = QLabel(self.frame_2)
        self.passwordLabel_2.setObjectName("passwordLabel_2")
        self.verticalLayout_5.addWidget(self.passwordLabel_2)
        self.PasswordEdit = QLineEdit(self.frame_2)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.verticalLayout_5.addWidget(self.PasswordEdit)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
        self.loginBtn = QPushButton(self.frame_2)
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout_5.addWidget(self.loginBtn)
        self.loginReqBtn_2 = QPushButton(self.frame_2)
        self.loginReqBtn_2.setObjectName("loginReqBtn_2")
        self.verticalLayout_5.addWidget(self.loginReqBtn_2)
        self.ForgotPwordBtn = QPushButton(self.frame_2)
        self.ForgotPwordBtn.setFlat(False)
        self.ForgotPwordBtn.setObjectName("ForgotPwordBtn")
        self.verticalLayout_5.addWidget(self.ForgotPwordBtn)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.loginPage)
        self.resetPage = QWidget()
        self.resetPage.setObjectName("resetPage")
        self.verticalLayout_9 = QVBoxLayout(self.resetPage)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QFrame(self.resetPage)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.Icon_3 = QLabel(self.frame_3)
        self.Icon_3.setMaximumSize(QSize(120, 81))
        self.Icon_3.setText("")
        self.Icon_3.setPixmap(QPixmap(":/futminna_logo"))
        self.Icon_3.setAlignment(Qt.AlignCenter)
        self.Icon_3.setObjectName("Icon_3")
        self.horizontalLayout_3.addWidget(self.Icon_3)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setStyleSheet("color:rgb(75, 75, 75);\n"
"font: 16pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.line_3 = QFrame(self.frame_3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.pword = QLineEdit(self.frame_3)
        self.pword.setObjectName("pword")
        self.verticalLayout_8.addWidget(self.pword)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.confirmPword = QLineEdit(self.frame_3)
        self.confirmPword.setObjectName("confirmPword")
        self.verticalLayout_8.addWidget(self.confirmPword)
        spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem9)
        self.resetPwordBtn = QPushButton(self.frame_3)
        self.resetPwordBtn.setObjectName("resetPwordBtn")
        self.verticalLayout_8.addWidget(self.resetPwordBtn)
        spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem10)
        self.line_4 = QFrame(self.frame_3)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.loginRetBtn = QPushButton(self.frame_3)
        self.loginRetBtn.setObjectName("loginRetBtn")
        self.verticalLayout_8.addWidget(self.loginRetBtn)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.resetPage)
        self.recover_page = QWidget()
        self.recover_page.setObjectName("recover_page")
        self.verticalLayout_12 = QVBoxLayout(self.recover_page)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_4 = QFrame(self.recover_page)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Icon_4 = QLabel(self.frame_4)
        self.Icon_4.setMaximumSize(QSize(120, 81))
        self.Icon_4.setText("")
        self.Icon_4.setPixmap(QPixmap(":/logo/futminna2.png"))
        self.Icon_4.setAlignment(Qt.AlignCenter)
        self.Icon_4.setObjectName("Icon_4")
        self.horizontalLayout_4.addWidget(self.Icon_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem11)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setStyleSheet("color:rgb(75, 75, 75);\n"
"font: 16pt \"Comic Sans MS\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem12)
        self.line_5 = QFrame(self.frame_4)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_10.addWidget(self.line_5)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.confirmEmail = QLineEdit(self.frame_4)
        self.confirmEmail.setObjectName("confirmEmail")
        self.verticalLayout_11.addWidget(self.confirmEmail)
        spacerItem13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem13)
        self.confirmBtn = QPushButton(self.frame_4)
        self.confirmBtn.setObjectName("confirmBtn")
        self.verticalLayout_11.addWidget(self.confirmBtn)
        spacerItem14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem14)
        self.loginRetBtn_2 = QPushButton(self.frame_4)
        self.loginRetBtn_2.setObjectName("loginRetBtn_2")
        self.verticalLayout_11.addWidget(self.loginRetBtn_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.recover_page)
        self.confirm_page = QWidget()
        self.confirm_page.setObjectName("confirm_page")
        self.verticalLayout_200 = QVBoxLayout(self.confirm_page)
        self.verticalLayout_200.setObjectName("verticalLayout_200")
        self.frame_12 = QFrame(self.confirm_page)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_196 = QVBoxLayout(self.frame_12)
        self.verticalLayout_196.setObjectName("verticalLayout_196")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Icon_5 = QLabel(self.frame_12)
        self.Icon_5.setMaximumSize(QSize(120, 81))
        self.Icon_5.setText("")
        self.Icon_5.setPixmap(QPixmap(":/futminna_logo"))
        self.Icon_5.setAlignment(Qt.AlignCenter)
        self.Icon_5.setObjectName("Icon_5")
        self.horizontalLayout_14.addWidget(self.Icon_5)
        self.verticalLayout_196.addLayout(self.horizontalLayout_14)
        self.label_24 = QLabel(self.frame_12)
        self.label_24.setStyleSheet("color:rgb(75, 75, 75);\n"
"font: 16pt \"Comic Sans MS\";")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_196.addWidget(self.label_24)
        self.line_6 = QFrame(self.frame_12)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_196.addWidget(self.line_6)
        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_196.addWidget(self.label_25)
        self.verticalLayout_199 = QVBoxLayout()
        self.verticalLayout_199.setObjectName("verticalLayout_199")
        self.label_26 = QLabel(self.frame_12)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_199.addWidget(self.label_26)
        self.confirmEmail_2 = QLineEdit(self.frame_12)
        self.confirmEmail_2.setObjectName("confirmEmail_2")
        self.verticalLayout_199.addWidget(self.confirmEmail_2)
        spacerItem15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_199.addItem(spacerItem15)
        self.confirmBtn_2 = QPushButton(self.frame_12)
        self.confirmBtn_2.setObjectName("confirmBtn_2")
        self.verticalLayout_199.addWidget(self.confirmBtn_2)
        spacerItem16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_199.addItem(spacerItem16)
        self.line_7 = QFrame(self.frame_12)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_199.addWidget(self.line_7)
        self.loginRetBtn_3 = QPushButton(self.frame_12)
        self.loginRetBtn_3.setObjectName("loginRetBtn_3")
        self.verticalLayout_199.addWidget(self.loginRetBtn_3)
        self.verticalLayout_196.addLayout(self.verticalLayout_199)
        self.verticalLayout_200.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.confirm_page)
        self.student_home = QWidget()
        self.student_home.setObjectName("student_home")
        self.verticalLayout_189 = QVBoxLayout(self.student_home)
        self.verticalLayout_189.setObjectName("verticalLayout_189")
        self.frame_5 = QFrame(self.student_home)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setText("")
        self.label_10.setPixmap(QPixmap(":/futminna"))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.textBrowser = QTextBrowser(self.frame_5)
        self.textBrowser.setStyleSheet("border: 2px dashed #efefef;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_13.addWidget(self.textBrowser)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 10%;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.tableWidget = QTableWidget(self.frame_5)
        self.tableWidget.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"font: 10pt \"Comic Sans MS\";")
        self.tableWidget.setAutoScrollMargin(15)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(242)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_13.addWidget(self.tableWidget)
        self.availSessionBtn = QPushButton(self.frame_5)
        self.availSessionBtn.setObjectName("availSessionBtn")
        self.verticalLayout_13.addWidget(self.availSessionBtn)
        self.label_10.raise_()
        self.label_11.raise_()
        self.availSessionBtn.raise_()
        self.tableWidget.raise_()
        self.textBrowser.raise_()
        self.verticalLayout_189.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.student_home)
        self.cr_home = QWidget()
        self.cr_home.setObjectName("cr_home")
        self.verticalLayout_16 = QVBoxLayout(self.cr_home)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_6 = QFrame(self.cr_home)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setText("")
        self.label_12.setPixmap(QPixmap(":/futminna"))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12)
        self.textBrowser_136 = QTextBrowser(self.frame_6)
        self.textBrowser_136.setStyleSheet("border: 2px dashed #efefef;")
        self.textBrowser_136.setObjectName("textBrowser_136")
        self.verticalLayout_14.addWidget(self.textBrowser_136)
        self.manageSessionBtn = QPushButton(self.frame_6)
        self.manageSessionBtn.setObjectName("manageSessionBtn")
        self.verticalLayout_14.addWidget(self.manageSessionBtn)
        self.verticalLayout_16.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.cr_home)
        self.create_session = QWidget()
        self.create_session.setObjectName("create_session")
        self.verticalLayout_188 = QVBoxLayout(self.create_session)
        self.verticalLayout_188.setObjectName("verticalLayout_188")
        self.frame_7 = QFrame(self.create_session)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_107 = QVBoxLayout(self.frame_7)
        self.verticalLayout_107.setObjectName("verticalLayout_107")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setStyleSheet("QMainWindow , QWidget{\n"
"    background-color: rgb(0, 170, 255);\n"
"    background-color: rgb(35, 134, 255);\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox {\n"
"border: 1px solid rgb(207, 207, 207);\n"
"font: 12pt \"Consolas\";\n"
"background-color: rgb(255, 255, 255);\n"
"margin: 1%;\n"
"padding: 4%;\n"
"}\n"
"\n"
"QLabel{\n"
"    \n"
"    font: 12pt \"Menlo\";\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid #ffffff;\n"
"    background-color: rgb(255, 92, 95);\n"
"    height: 2.8em;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgba(255, 148, 148, 234);\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(18, 18, 18);\n"
"    height:2.8em;\n"
"    color: #ffffff;\n"
"    font: 10pt \"Consolas\";\n"
"    border-radius: 3px;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(13, 13, 13);\n"
"    color: #000000;\n"
"    \n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_191 = QVBoxLayout(self.frame_10)
        self.verticalLayout_191.setObjectName("verticalLayout_191")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.label_27 = QLabel(self.frame_10)
        self.label_27.setText("")
        self.label_27.setPixmap(QPixmap(":/images/futminna2_.png"))
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_11.addWidget(self.label_27)
        spacerItem18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.verticalLayout_191.addLayout(self.horizontalLayout_11)
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_191.addWidget(self.label_14)
        self.stackedWidget_5 = QStackedWidget(self.frame_10)
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_192 = QVBoxLayout(self.page_2)
        self.verticalLayout_192.setObjectName("verticalLayout_192")
        self.verticalLayout_193 = QVBoxLayout()
        self.verticalLayout_193.setObjectName("verticalLayout_193")
        self.courseList = QComboBox(self.page_2)
        self.courseList.setObjectName("courseList")
        self.courseList.addItem("")
        self.verticalLayout_193.addWidget(self.courseList)
        self.lecturerList = QComboBox(self.page_2)
        self.lecturerList.setObjectName("lecturerList")
        self.lecturerList.addItem("")
        self.verticalLayout_193.addWidget(self.lecturerList)
        self.lectHallList = QComboBox(self.page_2)
        self.lectHallList.setObjectName("lectHallList")
        self.lectHallList.addItem("")
        self.verticalLayout_193.addWidget(self.lectHallList)
        self.comboBox_2 = QComboBox(self.page_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_193.addWidget(self.comboBox_2)
        self.comboBox_3 = QComboBox(self.page_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_193.addWidget(self.comboBox_3)
        self.spinBox = QSpinBox(self.page_2)
        self.spinBox.setMinimum(2018)
        self.spinBox.setMaximum(2050)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_193.addWidget(self.spinBox)
        self.verticalLayout_192.addLayout(self.verticalLayout_193)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.timeSpinBox = QSpinBox(self.page_2)
        self.timeSpinBox.setMinimum(1)
        self.timeSpinBox.setMaximum(12)
        self.timeSpinBox.setProperty("value", 9)
        self.timeSpinBox.setObjectName("timeSpinBox")
        self.horizontalLayout_12.addWidget(self.timeSpinBox)
        self.timeStamp = QComboBox(self.page_2)
        self.timeStamp.setObjectName("timeStamp")
        self.timeStamp.addItem("")
        self.timeStamp.addItem("")
        self.horizontalLayout_12.addWidget(self.timeStamp)
        self.verticalLayout_192.addLayout(self.horizontalLayout_12)
        spacerItem19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_192.addItem(spacerItem19)
        self.createSessionBtn = QPushButton(self.page_2)
        self.createSessionBtn.setObjectName("createSessionBtn")
        self.verticalLayout_192.addWidget(self.createSessionBtn)
        self.stackedWidget_5.addWidget(self.page_2)
        self.page_11 = QWidget()
        self.page_11.setObjectName("page_11")
        self.verticalLayout_17 = QVBoxLayout(self.page_11)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem20)
        self.verticalLayout_194 = QVBoxLayout()
        self.verticalLayout_194.setObjectName("verticalLayout_194")
        spacerItem21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_194.addItem(spacerItem21)
        self.closeCourseName = QLabel(self.page_11)
        self.closeCourseName.setObjectName("closeCourseName")
        self.verticalLayout_194.addWidget(self.closeCourseName)
        self.closeLecturerLabel = QLabel(self.page_11)
        self.closeLecturerLabel.setObjectName("closeLecturerLabel")
        self.verticalLayout_194.addWidget(self.closeLecturerLabel)
        self.lectureHallLabel = QLabel(self.page_11)
        self.lectureHallLabel.setObjectName("lectureHallLabel")
        self.verticalLayout_194.addWidget(self.lectureHallLabel)
        self.timeLabel = QLabel(self.page_11)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_194.addWidget(self.timeLabel)
        self.no_students = QLabel(self.page_11)
        self.no_students.setObjectName("no_students")
        self.verticalLayout_194.addWidget(self.no_students)
        spacerItem22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_194.addItem(spacerItem22)
        spacerItem23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_194.addItem(spacerItem23)
        self.textBrowser_137 = QTextBrowser(self.page_11)
        self.textBrowser_137.setStyleSheet("")
        self.textBrowser_137.setObjectName("textBrowser_137")
        self.verticalLayout_194.addWidget(self.textBrowser_137)
        spacerItem24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_194.addItem(spacerItem24)
        self.verticalLayout_17.addLayout(self.verticalLayout_194)
        self.closeSessionBtn = QPushButton(self.page_11)
        self.closeSessionBtn.setObjectName("closeSessionBtn")
        self.verticalLayout_17.addWidget(self.closeSessionBtn)
        self.stackedWidget_5.addWidget(self.page_11)
        self.verticalLayout_191.addWidget(self.stackedWidget_5)
        self.verticalLayout_107.addWidget(self.frame_10)
        self.verticalLayout_188.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.create_session)
        self.review_page = QWidget()
        self.review_page.setObjectName("review_page")
        self.verticalLayout_187 = QVBoxLayout(self.review_page)
        self.verticalLayout_187.setObjectName("verticalLayout_187")
        self.frame_8 = QFrame(self.review_page)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem25)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setText("")
        self.label_15.setPixmap(QPixmap(":/futminna_logo"))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        spacerItem26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem26)
        self.verticalLayout_15.addLayout(self.horizontalLayout_5)
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16)
        self.stackedWidget_2 = QStackedWidget(self.frame_8)
        self.stackedWidget_2.setStyleSheet("QLabel{\n"
"    \n"
"    font: 10pt \"Fira Code\";\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_18 = QVBoxLayout(self.page_3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.textBrowser_2 = QTextBrowser(self.page_3)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_18.addWidget(self.textBrowser_2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_3 = QTextBrowser(self.page_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 1, 0, 1, 1)
        self.a = QLabel(self.page_3)
        self.a.setObjectName("a")
        self.gridLayout.addWidget(self.a, 0, 1, 1, 1)
        self.textBrowser_5 = QTextBrowser(self.page_3)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 3, 0, 1, 1)
        self.textBrowser_4 = QTextBrowser(self.page_3)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 0, 0, 1, 1)
        self.d = QLabel(self.page_3)
        self.d.setObjectName("d")
        self.gridLayout.addWidget(self.d, 3, 1, 1, 1)
        self.c = QLabel(self.page_3)
        self.c.setObjectName("c")
        self.gridLayout.addWidget(self.c, 2, 1, 1, 1)
        self.b = QLabel(self.page_3)
        self.b.setObjectName("b")
        self.gridLayout.addWidget(self.b, 1, 1, 1, 1)
        self.textBrowser_6 = QTextBrowser(self.page_3)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 2, 0, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_19 = QVBoxLayout(self.page_4)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.textBrowser_48 = QTextBrowser(self.page_4)
        self.textBrowser_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_48.setObjectName("textBrowser_48")
        self.verticalLayout_19.addWidget(self.textBrowser_48)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.h_2 = QLabel(self.page_4)
        self.h_2.setObjectName("h_2")
        self.gridLayout_7.addWidget(self.h_2, 3, 1, 1, 1)
        self.f_2 = QLabel(self.page_4)
        self.f_2.setObjectName("f_2")
        self.gridLayout_7.addWidget(self.f_2, 1, 1, 1, 1)
        self.textBrowser_33 = QTextBrowser(self.page_4)
        self.textBrowser_33.setObjectName("textBrowser_33")
        self.gridLayout_7.addWidget(self.textBrowser_33, 2, 0, 1, 1)
        self.e_2 = QLabel(self.page_4)
        self.e_2.setObjectName("e_2")
        self.gridLayout_7.addWidget(self.e_2, 0, 1, 1, 1)
        self.g_2 = QLabel(self.page_4)
        self.g_2.setObjectName("g_2")
        self.gridLayout_7.addWidget(self.g_2, 2, 1, 1, 1)
        self.textBrowser_35 = QTextBrowser(self.page_4)
        self.textBrowser_35.setObjectName("textBrowser_35")
        self.gridLayout_7.addWidget(self.textBrowser_35, 3, 0, 1, 1)
        self.textBrowser_30 = QTextBrowser(self.page_4)
        self.textBrowser_30.setObjectName("textBrowser_30")
        self.gridLayout_7.addWidget(self.textBrowser_30, 1, 0, 1, 1)
        self.textBrowser_32 = QTextBrowser(self.page_4)
        self.textBrowser_32.setObjectName("textBrowser_32")
        self.gridLayout_7.addWidget(self.textBrowser_32, 0, 0, 1, 1)
        self.verticalLayout_19.addLayout(self.gridLayout_7)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_20 = QVBoxLayout(self.page_7)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.textBrowser_49 = QTextBrowser(self.page_7)
        self.textBrowser_49.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_49.setObjectName("textBrowser_49")
        self.verticalLayout_20.addWidget(self.textBrowser_49)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_11 = QTextBrowser(self.page_7)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.gridLayout_6.addWidget(self.textBrowser_11, 2, 0, 1, 1)
        self.k_2 = QLabel(self.page_7)
        self.k_2.setObjectName("k_2")
        self.gridLayout_6.addWidget(self.k_2, 2, 1, 1, 1)
        self.i = QLabel(self.page_7)
        self.i.setObjectName("i")
        self.gridLayout_6.addWidget(self.i, 0, 1, 1, 1)
        self.j_2 = QLabel(self.page_7)
        self.j_2.setObjectName("j_2")
        self.gridLayout_6.addWidget(self.j_2, 1, 1, 1, 1)
        self.textBrowser_8 = QTextBrowser(self.page_7)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout_6.addWidget(self.textBrowser_8, 1, 0, 1, 1)
        self.textBrowser_9 = QTextBrowser(self.page_7)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.gridLayout_6.addWidget(self.textBrowser_9, 0, 0, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_6)
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_5 = QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_21 = QVBoxLayout(self.page_5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.textBrowser_34 = QTextBrowser(self.page_5)
        self.textBrowser_34.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_34.setObjectName("textBrowser_34")
        self.verticalLayout_21.addWidget(self.textBrowser_34)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.k = QLabel(self.page_5)
        self.k.setObjectName("k")
        self.gridLayout_3.addWidget(self.k, 1, 1, 1, 1)
        self.textBrowser_15 = QTextBrowser(self.page_5)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.gridLayout_3.addWidget(self.textBrowser_15, 3, 0, 1, 1)
        self.l = QLabel(self.page_5)
        self.l.setObjectName("l")
        self.gridLayout_3.addWidget(self.l, 3, 1, 1, 1)
        self.textBrowser_13 = QTextBrowser(self.page_5)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout_3.addWidget(self.textBrowser_13, 1, 0, 1, 1)
        self.textBrowser_14 = QTextBrowser(self.page_5)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.gridLayout_3.addWidget(self.textBrowser_14, 0, 0, 1, 1)
        self.j = QLabel(self.page_5)
        self.j.setObjectName("j")
        self.gridLayout_3.addWidget(self.j, 0, 1, 1, 1)
        self.verticalLayout_21.addLayout(self.gridLayout_3)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_22 = QVBoxLayout(self.page_6)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.textBrowser_28 = QTextBrowser(self.page_6)
        self.textBrowser_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.verticalLayout_22.addWidget(self.textBrowser_28)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_18 = QTextBrowser(self.page_6)
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.gridLayout_4.addWidget(self.textBrowser_18, 3, 0, 1, 1)
        self.textBrowser_17 = QTextBrowser(self.page_6)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.gridLayout_4.addWidget(self.textBrowser_17, 2, 0, 1, 1)
        self.o = QLabel(self.page_6)
        self.o.setObjectName("o")
        self.gridLayout_4.addWidget(self.o, 3, 1, 1, 1)
        self.n = QLabel(self.page_6)
        self.n.setObjectName("n")
        self.gridLayout_4.addWidget(self.n, 2, 1, 1, 1)
        self.textBrowser_19 = QTextBrowser(self.page_6)
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.gridLayout_4.addWidget(self.textBrowser_19, 4, 0, 1, 1)
        self.p = QLabel(self.page_6)
        self.p.setObjectName("p")
        self.gridLayout_4.addWidget(self.p, 4, 1, 1, 1)
        self.textBrowser_16 = QTextBrowser(self.page_6)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.gridLayout_4.addWidget(self.textBrowser_16, 1, 0, 1, 1)
        self.m = QLabel(self.page_6)
        self.m.setObjectName("m")
        self.gridLayout_4.addWidget(self.m, 1, 1, 1, 1)
        self.verticalLayout_22.addLayout(self.gridLayout_4)
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_8 = QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_23 = QVBoxLayout(self.page_8)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.textBrowser_20 = QTextBrowser(self.page_8)
        self.textBrowser_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.verticalLayout_23.addWidget(self.textBrowser_20)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.s = QLabel(self.page_8)
        self.s.setObjectName("s")
        self.gridLayout_5.addWidget(self.s, 2, 1, 1, 1)
        self.textBrowser_26 = QTextBrowser(self.page_8)
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.gridLayout_5.addWidget(self.textBrowser_26, 1, 0, 1, 1)
        self.t = QLabel(self.page_8)
        self.t.setObjectName("t")
        self.gridLayout_5.addWidget(self.t, 3, 1, 1, 1)
        self.textBrowser_24 = QTextBrowser(self.page_8)
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.gridLayout_5.addWidget(self.textBrowser_24, 3, 0, 1, 1)
        self.r = QLabel(self.page_8)
        self.r.setObjectName("r")
        self.gridLayout_5.addWidget(self.r, 1, 1, 1, 1)
        self.textBrowser_25 = QTextBrowser(self.page_8)
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.gridLayout_5.addWidget(self.textBrowser_25, 2, 0, 1, 1)
        self.textBrowser_27 = QTextBrowser(self.page_8)
        self.textBrowser_27.setObjectName("textBrowser_27")
        self.gridLayout_5.addWidget(self.textBrowser_27, 0, 0, 1, 1)
        self.q = QLabel(self.page_8)
        self.q.setObjectName("q")
        self.gridLayout_5.addWidget(self.q, 0, 1, 1, 1)
        self.verticalLayout_23.addLayout(self.gridLayout_5)
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_24 = QVBoxLayout(self.page_9)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.textBrowser_29 = QTextBrowser(self.page_9)
        self.textBrowser_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_29.setObjectName("textBrowser_29")
        self.verticalLayout_24.addWidget(self.textBrowser_29)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.v = QLabel(self.page_9)
        self.v.setObjectName("v")
        self.gridLayout_8.addWidget(self.v, 1, 1, 1, 1)
        self.textBrowser_22 = QTextBrowser(self.page_9)
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.gridLayout_8.addWidget(self.textBrowser_22, 1, 0, 1, 1)
        self.textBrowser_21 = QTextBrowser(self.page_9)
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.gridLayout_8.addWidget(self.textBrowser_21, 2, 0, 1, 1)
        self.u = QLabel(self.page_9)
        self.u.setObjectName("u")
        self.gridLayout_8.addWidget(self.u, 0, 1, 1, 1)
        self.w = QLabel(self.page_9)
        self.w.setObjectName("w")
        self.gridLayout_8.addWidget(self.w, 2, 1, 1, 1)
        self.textBrowser_23 = QTextBrowser(self.page_9)
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.gridLayout_8.addWidget(self.textBrowser_23, 0, 0, 1, 1)
        self.verticalLayout_24.addLayout(self.gridLayout_8)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_25 = QVBoxLayout(self.page_10)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.uploadBtn = QPushButton(self.page_10)
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayout_25.addWidget(self.uploadBtn)
        self.discardBtn = QPushButton(self.page_10)
        self.discardBtn.setObjectName("discardBtn")
        self.verticalLayout_25.addWidget(self.discardBtn)
        spacerItem27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem27)
        spacerItem28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem28)
        spacerItem29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem29)
        self.stackedWidget_2.addWidget(self.page_10)
        self.verticalLayout_15.addWidget(self.stackedWidget_2)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.prevBtn = QPushButton(self.frame_8)
        self.prevBtn.setObjectName("prevBtn")
        self.horizontalLayout_6.addWidget(self.prevBtn)
        spacerItem30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem30)
        self.nextBtn = QPushButton(self.frame_8)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_6.addWidget(self.nextBtn)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.verticalLayout_187.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.review_page)
        self.grading_page = QWidget()
        self.grading_page.setObjectName("grading_page")
        self.verticalLayout_186 = QVBoxLayout(self.grading_page)
        self.verticalLayout_186.setObjectName("verticalLayout_186")
        self.frame_9 = QFrame(self.grading_page)
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_106 = QVBoxLayout(self.frame_9)
        self.verticalLayout_106.setObjectName("verticalLayout_106")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem31)
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setText("")
        self.label_20.setPixmap(QPixmap(":/images/futminna2_.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        spacerItem32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem32)
        self.verticalLayout_106.addLayout(self.horizontalLayout_9)
        self.verticalLayout_108 = QVBoxLayout()
        self.verticalLayout_108.setObjectName("verticalLayout_108")
        self.course_code_2 = QLabel(self.frame_9)
        self.course_code_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 2px;")
        self.course_code_2.setObjectName("course_code_2")
        self.verticalLayout_108.addWidget(self.course_code_2)
        self.course_2 = QLabel(self.frame_9)
        self.course_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 2px;")
        self.course_2.setObjectName("course_2")
        self.verticalLayout_108.addWidget(self.course_2)
        self.lecturer_2 = QLabel(self.frame_9)
        self.lecturer_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 2px;")
        self.lecturer_2.setObjectName("lecturer_2")
        self.verticalLayout_108.addWidget(self.lecturer_2)
        self.lectHall_2 = QLabel(self.frame_9)
        self.lectHall_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"padding: 2px;")
        self.lectHall_2.setObjectName("lectHall_2")
        self.verticalLayout_108.addWidget(self.lectHall_2)
        self.stackedWidget_4 = QStackedWidget(self.frame_9)
        self.stackedWidget_4.setStyleSheet("background-color: rgb(45, 99, 99);\n"
"font: 10pt \"Comic Sans MS\";")
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_39 = QWidget()
        self.page_39.setObjectName("page_39")
        self.verticalLayout_109 = QVBoxLayout(self.page_39)
        self.verticalLayout_109.setObjectName("verticalLayout_109")
        self.textBrowser_85 = QTextBrowser(self.page_39)
        self.textBrowser_85.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_85.setObjectName("textBrowser_85")
        self.verticalLayout_109.addWidget(self.textBrowser_85)
        self.textBrowser_86 = QTextBrowser(self.page_39)
        self.textBrowser_86.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_86.setObjectName("textBrowser_86")
        self.verticalLayout_109.addWidget(self.textBrowser_86)
        self.groupBox_5 = QGroupBox(self.page_39)
        self.groupBox_5.setStyleSheet("")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_110 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_110.setObjectName("verticalLayout_110")
        self.verticalLayout_111 = QVBoxLayout()
        self.verticalLayout_111.setObjectName("verticalLayout_111")
        self.radioButton_1_6 = QRadioButton(self.groupBox_5)
        self.radioButton_1_6.setStyleSheet("")
        self.radioButton_1_6.setObjectName("radioButton_1_6")
        self.verticalLayout_111.addWidget(self.radioButton_1_6)
        self.radioButton_1_7 = QRadioButton(self.groupBox_5)
        self.radioButton_1_7.setObjectName("radioButton_1_7")
        self.verticalLayout_111.addWidget(self.radioButton_1_7)
        self.radioButton_1_8 = QRadioButton(self.groupBox_5)
        self.radioButton_1_8.setObjectName("radioButton_1_8")
        self.verticalLayout_111.addWidget(self.radioButton_1_8)
        self.radioButton_1_9 = QRadioButton(self.groupBox_5)
        self.radioButton_1_9.setObjectName("radioButton_1_9")
        self.verticalLayout_111.addWidget(self.radioButton_1_9)
        self.radioButton_1_10 = QRadioButton(self.groupBox_5)
        self.radioButton_1_10.setObjectName("radioButton_1_10")
        self.verticalLayout_111.addWidget(self.radioButton_1_10)
        self.verticalLayout_110.addLayout(self.verticalLayout_111)
        self.verticalLayout_109.addWidget(self.groupBox_5)
        self.stackedWidget_4.addWidget(self.page_39)
        self.page_40 = QWidget()
        self.page_40.setObjectName("page_40")
        self.verticalLayout_112 = QVBoxLayout(self.page_40)
        self.verticalLayout_112.setObjectName("verticalLayout_112")
        self.textBrowser_87 = QTextBrowser(self.page_40)
        self.textBrowser_87.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_87.setObjectName("textBrowser_87")
        self.verticalLayout_112.addWidget(self.textBrowser_87)
        self.textBrowser_88 = QTextBrowser(self.page_40)
        self.textBrowser_88.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_88.setObjectName("textBrowser_88")
        self.verticalLayout_112.addWidget(self.textBrowser_88)
        self.groupBox_28 = QGroupBox(self.page_40)
        self.groupBox_28.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_28.setFlat(False)
        self.groupBox_28.setObjectName("groupBox_28")
        self.verticalLayout_113 = QVBoxLayout(self.groupBox_28)
        self.verticalLayout_113.setObjectName("verticalLayout_113")
        self.verticalLayout_114 = QVBoxLayout()
        self.verticalLayout_114.setObjectName("verticalLayout_114")
        self.radioButton_2_6 = QRadioButton(self.groupBox_28)
        self.radioButton_2_6.setStyleSheet("")
        self.radioButton_2_6.setObjectName("radioButton_2_6")
        self.verticalLayout_114.addWidget(self.radioButton_2_6)
        self.radioButton_2_7 = QRadioButton(self.groupBox_28)
        self.radioButton_2_7.setObjectName("radioButton_2_7")
        self.verticalLayout_114.addWidget(self.radioButton_2_7)
        self.radioButton_2_8 = QRadioButton(self.groupBox_28)
        self.radioButton_2_8.setObjectName("radioButton_2_8")
        self.verticalLayout_114.addWidget(self.radioButton_2_8)
        self.radioButton_2_9 = QRadioButton(self.groupBox_28)
        self.radioButton_2_9.setObjectName("radioButton_2_9")
        self.verticalLayout_114.addWidget(self.radioButton_2_9)
        self.radioButton_2_10 = QRadioButton(self.groupBox_28)
        self.radioButton_2_10.setObjectName("radioButton_2_10")
        self.verticalLayout_114.addWidget(self.radioButton_2_10)
        self.verticalLayout_113.addLayout(self.verticalLayout_114)
        self.verticalLayout_112.addWidget(self.groupBox_28)
        self.stackedWidget_4.addWidget(self.page_40)
        self.page_41 = QWidget()
        self.page_41.setObjectName("page_41")
        self.verticalLayout_115 = QVBoxLayout(self.page_41)
        self.verticalLayout_115.setObjectName("verticalLayout_115")
        self.textBrowser_89 = QTextBrowser(self.page_41)
        self.textBrowser_89.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_89.setObjectName("textBrowser_89")
        self.verticalLayout_115.addWidget(self.textBrowser_89)
        self.textBrowser_90 = QTextBrowser(self.page_41)
        self.textBrowser_90.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_90.setObjectName("textBrowser_90")
        self.verticalLayout_115.addWidget(self.textBrowser_90)
        self.groupBox_29 = QGroupBox(self.page_41)
        self.groupBox_29.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_29.setFlat(False)
        self.groupBox_29.setObjectName("groupBox_29")
        self.verticalLayout_116 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_116.setObjectName("verticalLayout_116")
        self.verticalLayout_117 = QVBoxLayout()
        self.verticalLayout_117.setObjectName("verticalLayout_117")
        self.radioButton_3_6 = QRadioButton(self.groupBox_29)
        self.radioButton_3_6.setStyleSheet("")
        self.radioButton_3_6.setObjectName("radioButton_3_6")
        self.verticalLayout_117.addWidget(self.radioButton_3_6)
        self.radioButton_3_7 = QRadioButton(self.groupBox_29)
        self.radioButton_3_7.setObjectName("radioButton_3_7")
        self.verticalLayout_117.addWidget(self.radioButton_3_7)
        self.radioButton_3_8 = QRadioButton(self.groupBox_29)
        self.radioButton_3_8.setObjectName("radioButton_3_8")
        self.verticalLayout_117.addWidget(self.radioButton_3_8)
        self.radioButton_3_9 = QRadioButton(self.groupBox_29)
        self.radioButton_3_9.setObjectName("radioButton_3_9")
        self.verticalLayout_117.addWidget(self.radioButton_3_9)
        self.radioButton_3_10 = QRadioButton(self.groupBox_29)
        self.radioButton_3_10.setObjectName("radioButton_3_10")
        self.verticalLayout_117.addWidget(self.radioButton_3_10)
        self.verticalLayout_116.addLayout(self.verticalLayout_117)
        self.verticalLayout_115.addWidget(self.groupBox_29)
        self.stackedWidget_4.addWidget(self.page_41)
        self.page_42 = QWidget()
        self.page_42.setObjectName("page_42")
        self.verticalLayout_118 = QVBoxLayout(self.page_42)
        self.verticalLayout_118.setObjectName("verticalLayout_118")
        self.textBrowser_91 = QTextBrowser(self.page_42)
        self.textBrowser_91.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_91.setObjectName("textBrowser_91")
        self.verticalLayout_118.addWidget(self.textBrowser_91)
        self.textBrowser_92 = QTextBrowser(self.page_42)
        self.textBrowser_92.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_92.setObjectName("textBrowser_92")
        self.verticalLayout_118.addWidget(self.textBrowser_92)
        self.groupBox_30 = QGroupBox(self.page_42)
        self.groupBox_30.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_30.setFlat(False)
        self.groupBox_30.setObjectName("groupBox_30")
        self.verticalLayout_119 = QVBoxLayout(self.groupBox_30)
        self.verticalLayout_119.setObjectName("verticalLayout_119")
        self.verticalLayout_120 = QVBoxLayout()
        self.verticalLayout_120.setObjectName("verticalLayout_120")
        self.radioButton_4_6 = QRadioButton(self.groupBox_30)
        self.radioButton_4_6.setStyleSheet("")
        self.radioButton_4_6.setObjectName("radioButton_4_6")
        self.verticalLayout_120.addWidget(self.radioButton_4_6)
        self.radioButton_4_7 = QRadioButton(self.groupBox_30)
        self.radioButton_4_7.setObjectName("radioButton_4_7")
        self.verticalLayout_120.addWidget(self.radioButton_4_7)
        self.radioButton_4_8 = QRadioButton(self.groupBox_30)
        self.radioButton_4_8.setObjectName("radioButton_4_8")
        self.verticalLayout_120.addWidget(self.radioButton_4_8)
        self.radioButton_4_9 = QRadioButton(self.groupBox_30)
        self.radioButton_4_9.setObjectName("radioButton_4_9")
        self.verticalLayout_120.addWidget(self.radioButton_4_9)
        self.radioButton_4_10 = QRadioButton(self.groupBox_30)
        self.radioButton_4_10.setObjectName("radioButton_4_10")
        self.verticalLayout_120.addWidget(self.radioButton_4_10)
        self.verticalLayout_119.addLayout(self.verticalLayout_120)
        self.verticalLayout_118.addWidget(self.groupBox_30)
        self.stackedWidget_4.addWidget(self.page_42)
        self.page_43 = QWidget()
        self.page_43.setObjectName("page_43")
        self.verticalLayout_121 = QVBoxLayout(self.page_43)
        self.verticalLayout_121.setObjectName("verticalLayout_121")
        self.textBrowser_93 = QTextBrowser(self.page_43)
        self.textBrowser_93.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_93.setObjectName("textBrowser_93")
        self.verticalLayout_121.addWidget(self.textBrowser_93)
        self.textBrowser_94 = QTextBrowser(self.page_43)
        self.textBrowser_94.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_94.setObjectName("textBrowser_94")
        self.verticalLayout_121.addWidget(self.textBrowser_94)
        self.groupBox_31 = QGroupBox(self.page_43)
        self.groupBox_31.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_31.setFlat(False)
        self.groupBox_31.setObjectName("groupBox_31")
        self.verticalLayout_122 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_122.setObjectName("verticalLayout_122")
        self.verticalLayout_123 = QVBoxLayout()
        self.verticalLayout_123.setObjectName("verticalLayout_123")
        self.radioButton_5_6 = QRadioButton(self.groupBox_31)
        self.radioButton_5_6.setStyleSheet("")
        self.radioButton_5_6.setObjectName("radioButton_5_6")
        self.verticalLayout_123.addWidget(self.radioButton_5_6)
        self.radioButton_5_7 = QRadioButton(self.groupBox_31)
        self.radioButton_5_7.setObjectName("radioButton_5_7")
        self.verticalLayout_123.addWidget(self.radioButton_5_7)
        self.radioButton_5_8 = QRadioButton(self.groupBox_31)
        self.radioButton_5_8.setObjectName("radioButton_5_8")
        self.verticalLayout_123.addWidget(self.radioButton_5_8)
        self.radioButton_5_9 = QRadioButton(self.groupBox_31)
        self.radioButton_5_9.setObjectName("radioButton_5_9")
        self.verticalLayout_123.addWidget(self.radioButton_5_9)
        self.radioButton_5_10 = QRadioButton(self.groupBox_31)
        self.radioButton_5_10.setObjectName("radioButton_5_10")
        self.verticalLayout_123.addWidget(self.radioButton_5_10)
        self.verticalLayout_122.addLayout(self.verticalLayout_123)
        self.verticalLayout_121.addWidget(self.groupBox_31)
        self.stackedWidget_4.addWidget(self.page_43)
        self.page_44 = QWidget()
        self.page_44.setObjectName("page_44")
        self.verticalLayout_124 = QVBoxLayout(self.page_44)
        self.verticalLayout_124.setObjectName("verticalLayout_124")
        self.textBrowser_95 = QTextBrowser(self.page_44)
        self.textBrowser_95.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_95.setObjectName("textBrowser_95")
        self.verticalLayout_124.addWidget(self.textBrowser_95)
        self.textBrowser_96 = QTextBrowser(self.page_44)
        self.textBrowser_96.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_96.setObjectName("textBrowser_96")
        self.verticalLayout_124.addWidget(self.textBrowser_96)
        self.groupBox_32 = QGroupBox(self.page_44)
        self.groupBox_32.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_32.setFlat(False)
        self.groupBox_32.setObjectName("groupBox_32")
        self.verticalLayout_125 = QVBoxLayout(self.groupBox_32)
        self.verticalLayout_125.setObjectName("verticalLayout_125")
        self.verticalLayout_126 = QVBoxLayout()
        self.verticalLayout_126.setObjectName("verticalLayout_126")
        self.radioButton_6_6 = QRadioButton(self.groupBox_32)
        self.radioButton_6_6.setStyleSheet("")
        self.radioButton_6_6.setObjectName("radioButton_6_6")
        self.verticalLayout_126.addWidget(self.radioButton_6_6)
        self.radioButton_6_7 = QRadioButton(self.groupBox_32)
        self.radioButton_6_7.setObjectName("radioButton_6_7")
        self.verticalLayout_126.addWidget(self.radioButton_6_7)
        self.radioButton_6_8 = QRadioButton(self.groupBox_32)
        self.radioButton_6_8.setObjectName("radioButton_6_8")
        self.verticalLayout_126.addWidget(self.radioButton_6_8)
        self.radioButton_6_9 = QRadioButton(self.groupBox_32)
        self.radioButton_6_9.setObjectName("radioButton_6_9")
        self.verticalLayout_126.addWidget(self.radioButton_6_9)
        self.radioButton_6_10 = QRadioButton(self.groupBox_32)
        self.radioButton_6_10.setObjectName("radioButton_6_10")
        self.verticalLayout_126.addWidget(self.radioButton_6_10)
        self.verticalLayout_125.addLayout(self.verticalLayout_126)
        self.verticalLayout_124.addWidget(self.groupBox_32)
        self.stackedWidget_4.addWidget(self.page_44)
        self.page_45 = QWidget()
        self.page_45.setObjectName("page_45")
        self.verticalLayout_127 = QVBoxLayout(self.page_45)
        self.verticalLayout_127.setObjectName("verticalLayout_127")
        self.textBrowser_97 = QTextBrowser(self.page_45)
        self.textBrowser_97.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_97.setObjectName("textBrowser_97")
        self.verticalLayout_127.addWidget(self.textBrowser_97)
        self.textBrowser_98 = QTextBrowser(self.page_45)
        self.textBrowser_98.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_98.setObjectName("textBrowser_98")
        self.verticalLayout_127.addWidget(self.textBrowser_98)
        self.groupBox_33 = QGroupBox(self.page_45)
        self.groupBox_33.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_33.setFlat(False)
        self.groupBox_33.setObjectName("groupBox_33")
        self.verticalLayout_128 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_128.setObjectName("verticalLayout_128")
        self.verticalLayout_129 = QVBoxLayout()
        self.verticalLayout_129.setObjectName("verticalLayout_129")
        self.radioButton_7_6 = QRadioButton(self.groupBox_33)
        self.radioButton_7_6.setStyleSheet("")
        self.radioButton_7_6.setObjectName("radioButton_7_6")
        self.verticalLayout_129.addWidget(self.radioButton_7_6)
        self.radioButton_7_7 = QRadioButton(self.groupBox_33)
        self.radioButton_7_7.setObjectName("radioButton_7_7")
        self.verticalLayout_129.addWidget(self.radioButton_7_7)
        self.radioButton_7_8 = QRadioButton(self.groupBox_33)
        self.radioButton_7_8.setObjectName("radioButton_7_8")
        self.verticalLayout_129.addWidget(self.radioButton_7_8)
        self.radioButton_7_9 = QRadioButton(self.groupBox_33)
        self.radioButton_7_9.setObjectName("radioButton_7_9")
        self.verticalLayout_129.addWidget(self.radioButton_7_9)
        self.radioButton_7_10 = QRadioButton(self.groupBox_33)
        self.radioButton_7_10.setObjectName("radioButton_7_10")
        self.verticalLayout_129.addWidget(self.radioButton_7_10)
        self.verticalLayout_128.addLayout(self.verticalLayout_129)
        self.verticalLayout_127.addWidget(self.groupBox_33)
        self.stackedWidget_4.addWidget(self.page_45)
        self.page_46 = QWidget()
        self.page_46.setObjectName("page_46")
        self.verticalLayout_130 = QVBoxLayout(self.page_46)
        self.verticalLayout_130.setObjectName("verticalLayout_130")
        self.textBrowser_99 = QTextBrowser(self.page_46)
        self.textBrowser_99.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_99.setObjectName("textBrowser_99")
        self.verticalLayout_130.addWidget(self.textBrowser_99)
        self.textBrowser_100 = QTextBrowser(self.page_46)
        self.textBrowser_100.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_100.setObjectName("textBrowser_100")
        self.verticalLayout_130.addWidget(self.textBrowser_100)
        self.groupBox_34 = QGroupBox(self.page_46)
        self.groupBox_34.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_34.setFlat(False)
        self.groupBox_34.setObjectName("groupBox_34")
        self.verticalLayout_131 = QVBoxLayout(self.groupBox_34)
        self.verticalLayout_131.setObjectName("verticalLayout_131")
        self.verticalLayout_132 = QVBoxLayout()
        self.verticalLayout_132.setObjectName("verticalLayout_132")
        self.radioButton_8_6 = QRadioButton(self.groupBox_34)
        self.radioButton_8_6.setStyleSheet("")
        self.radioButton_8_6.setObjectName("radioButton_8_6")
        self.verticalLayout_132.addWidget(self.radioButton_8_6)
        self.radioButton_8_7 = QRadioButton(self.groupBox_34)
        self.radioButton_8_7.setObjectName("radioButton_8_7")
        self.verticalLayout_132.addWidget(self.radioButton_8_7)
        self.radioButton_8_8 = QRadioButton(self.groupBox_34)
        self.radioButton_8_8.setObjectName("radioButton_8_8")
        self.verticalLayout_132.addWidget(self.radioButton_8_8)
        self.radioButton_8_9 = QRadioButton(self.groupBox_34)
        self.radioButton_8_9.setObjectName("radioButton_8_9")
        self.verticalLayout_132.addWidget(self.radioButton_8_9)
        self.radioButton_8_10 = QRadioButton(self.groupBox_34)
        self.radioButton_8_10.setObjectName("radioButton_8_10")
        self.verticalLayout_132.addWidget(self.radioButton_8_10)
        self.verticalLayout_131.addLayout(self.verticalLayout_132)
        self.verticalLayout_130.addWidget(self.groupBox_34)
        self.stackedWidget_4.addWidget(self.page_46)
        self.page_47 = QWidget()
        self.page_47.setObjectName("page_47")
        self.verticalLayout_133 = QVBoxLayout(self.page_47)
        self.verticalLayout_133.setObjectName("verticalLayout_133")
        self.textBrowser_101 = QTextBrowser(self.page_47)
        self.textBrowser_101.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_101.setObjectName("textBrowser_101")
        self.verticalLayout_133.addWidget(self.textBrowser_101)
        self.textBrowser_102 = QTextBrowser(self.page_47)
        self.textBrowser_102.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_102.setObjectName("textBrowser_102")
        self.verticalLayout_133.addWidget(self.textBrowser_102)
        self.groupBox_35 = QGroupBox(self.page_47)
        self.groupBox_35.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_35.setFlat(False)
        self.groupBox_35.setObjectName("groupBox_35")
        self.verticalLayout_134 = QVBoxLayout(self.groupBox_35)
        self.verticalLayout_134.setObjectName("verticalLayout_134")
        self.verticalLayout_135 = QVBoxLayout()
        self.verticalLayout_135.setObjectName("verticalLayout_135")
        self.radioButton_9_6 = QRadioButton(self.groupBox_35)
        self.radioButton_9_6.setStyleSheet("")
        self.radioButton_9_6.setObjectName("radioButton_9_6")
        self.verticalLayout_135.addWidget(self.radioButton_9_6)
        self.radioButton_9_7 = QRadioButton(self.groupBox_35)
        self.radioButton_9_7.setObjectName("radioButton_9_7")
        self.verticalLayout_135.addWidget(self.radioButton_9_7)
        self.radioButton_9_8 = QRadioButton(self.groupBox_35)
        self.radioButton_9_8.setObjectName("radioButton_9_8")
        self.verticalLayout_135.addWidget(self.radioButton_9_8)
        self.radioButton_9_9 = QRadioButton(self.groupBox_35)
        self.radioButton_9_9.setObjectName("radioButton_9_9")
        self.verticalLayout_135.addWidget(self.radioButton_9_9)
        self.radioButton_9_10 = QRadioButton(self.groupBox_35)
        self.radioButton_9_10.setObjectName("radioButton_9_10")
        self.verticalLayout_135.addWidget(self.radioButton_9_10)
        self.verticalLayout_134.addLayout(self.verticalLayout_135)
        self.verticalLayout_133.addWidget(self.groupBox_35)
        self.stackedWidget_4.addWidget(self.page_47)
        self.page_48 = QWidget()
        self.page_48.setObjectName("page_48")
        self.verticalLayout_136 = QVBoxLayout(self.page_48)
        self.verticalLayout_136.setObjectName("verticalLayout_136")
        self.textBrowser_103 = QTextBrowser(self.page_48)
        self.textBrowser_103.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_103.setObjectName("textBrowser_103")
        self.verticalLayout_136.addWidget(self.textBrowser_103)
        self.textBrowser_104 = QTextBrowser(self.page_48)
        self.textBrowser_104.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_104.setObjectName("textBrowser_104")
        self.verticalLayout_136.addWidget(self.textBrowser_104)
        self.groupBox_36 = QGroupBox(self.page_48)
        self.groupBox_36.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_36.setFlat(False)
        self.groupBox_36.setObjectName("groupBox_36")
        self.verticalLayout_137 = QVBoxLayout(self.groupBox_36)
        self.verticalLayout_137.setObjectName("verticalLayout_137")
        self.verticalLayout_138 = QVBoxLayout()
        self.verticalLayout_138.setObjectName("verticalLayout_138")
        self.radioButton_10_6 = QRadioButton(self.groupBox_36)
        self.radioButton_10_6.setStyleSheet("")
        self.radioButton_10_6.setObjectName("radioButton_10_6")
        self.verticalLayout_138.addWidget(self.radioButton_10_6)
        self.radioButton_10_7 = QRadioButton(self.groupBox_36)
        self.radioButton_10_7.setObjectName("radioButton_10_7")
        self.verticalLayout_138.addWidget(self.radioButton_10_7)
        self.radioButton_10_8 = QRadioButton(self.groupBox_36)
        self.radioButton_10_8.setObjectName("radioButton_10_8")
        self.verticalLayout_138.addWidget(self.radioButton_10_8)
        self.radioButton_10_9 = QRadioButton(self.groupBox_36)
        self.radioButton_10_9.setObjectName("radioButton_10_9")
        self.verticalLayout_138.addWidget(self.radioButton_10_9)
        self.radioButton_10_10 = QRadioButton(self.groupBox_36)
        self.radioButton_10_10.setObjectName("radioButton_10_10")
        self.verticalLayout_138.addWidget(self.radioButton_10_10)
        self.verticalLayout_137.addLayout(self.verticalLayout_138)
        self.verticalLayout_136.addWidget(self.groupBox_36)
        self.stackedWidget_4.addWidget(self.page_48)
        self.page_49 = QWidget()
        self.page_49.setObjectName("page_49")
        self.verticalLayout_139 = QVBoxLayout(self.page_49)
        self.verticalLayout_139.setObjectName("verticalLayout_139")
        self.textBrowser_105 = QTextBrowser(self.page_49)
        self.textBrowser_105.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_105.setObjectName("textBrowser_105")
        self.verticalLayout_139.addWidget(self.textBrowser_105)
        self.textBrowser_106 = QTextBrowser(self.page_49)
        self.textBrowser_106.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_106.setObjectName("textBrowser_106")
        self.verticalLayout_139.addWidget(self.textBrowser_106)
        self.groupBox_37 = QGroupBox(self.page_49)
        self.groupBox_37.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_37.setFlat(False)
        self.groupBox_37.setObjectName("groupBox_37")
        self.verticalLayout_140 = QVBoxLayout(self.groupBox_37)
        self.verticalLayout_140.setObjectName("verticalLayout_140")
        self.verticalLayout_141 = QVBoxLayout()
        self.verticalLayout_141.setObjectName("verticalLayout_141")
        self.radioButton_11_6 = QRadioButton(self.groupBox_37)
        self.radioButton_11_6.setStyleSheet("")
        self.radioButton_11_6.setObjectName("radioButton_11_6")
        self.verticalLayout_141.addWidget(self.radioButton_11_6)
        self.radioButton_11_7 = QRadioButton(self.groupBox_37)
        self.radioButton_11_7.setObjectName("radioButton_11_7")
        self.verticalLayout_141.addWidget(self.radioButton_11_7)
        self.radioButton_11_8 = QRadioButton(self.groupBox_37)
        self.radioButton_11_8.setObjectName("radioButton_11_8")
        self.verticalLayout_141.addWidget(self.radioButton_11_8)
        self.radioButton_11_9 = QRadioButton(self.groupBox_37)
        self.radioButton_11_9.setObjectName("radioButton_11_9")
        self.verticalLayout_141.addWidget(self.radioButton_11_9)
        self.radioButton_11_10 = QRadioButton(self.groupBox_37)
        self.radioButton_11_10.setObjectName("radioButton_11_10")
        self.verticalLayout_141.addWidget(self.radioButton_11_10)
        self.verticalLayout_140.addLayout(self.verticalLayout_141)
        self.verticalLayout_139.addWidget(self.groupBox_37)
        self.stackedWidget_4.addWidget(self.page_49)
        self.page_50 = QWidget()
        self.page_50.setObjectName("page_50")
        self.verticalLayout_142 = QVBoxLayout(self.page_50)
        self.verticalLayout_142.setObjectName("verticalLayout_142")
        self.textBrowser_107 = QTextBrowser(self.page_50)
        self.textBrowser_107.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_107.setObjectName("textBrowser_107")
        self.verticalLayout_142.addWidget(self.textBrowser_107)
        self.textBrowser_108 = QTextBrowser(self.page_50)
        self.textBrowser_108.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_108.setObjectName("textBrowser_108")
        self.verticalLayout_142.addWidget(self.textBrowser_108)
        self.groupBox_38 = QGroupBox(self.page_50)
        self.groupBox_38.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_38.setFlat(False)
        self.groupBox_38.setObjectName("groupBox_38")
        self.verticalLayout_143 = QVBoxLayout(self.groupBox_38)
        self.verticalLayout_143.setObjectName("verticalLayout_143")
        self.verticalLayout_144 = QVBoxLayout()
        self.verticalLayout_144.setObjectName("verticalLayout_144")
        self.radioButton_12_6 = QRadioButton(self.groupBox_38)
        self.radioButton_12_6.setStyleSheet("")
        self.radioButton_12_6.setObjectName("radioButton_12_6")
        self.verticalLayout_144.addWidget(self.radioButton_12_6)
        self.radioButton_12_7 = QRadioButton(self.groupBox_38)
        self.radioButton_12_7.setObjectName("radioButton_12_7")
        self.verticalLayout_144.addWidget(self.radioButton_12_7)
        self.radioButton_12_8 = QRadioButton(self.groupBox_38)
        self.radioButton_12_8.setObjectName("radioButton_12_8")
        self.verticalLayout_144.addWidget(self.radioButton_12_8)
        self.radioButton_12_9 = QRadioButton(self.groupBox_38)
        self.radioButton_12_9.setObjectName("radioButton_12_9")
        self.verticalLayout_144.addWidget(self.radioButton_12_9)
        self.radioButton_12_10 = QRadioButton(self.groupBox_38)
        self.radioButton_12_10.setObjectName("radioButton_12_10")
        self.verticalLayout_144.addWidget(self.radioButton_12_10)
        self.verticalLayout_143.addLayout(self.verticalLayout_144)
        self.verticalLayout_142.addWidget(self.groupBox_38)
        self.stackedWidget_4.addWidget(self.page_50)
        self.page_51 = QWidget()
        self.page_51.setObjectName("page_51")
        self.verticalLayout_145 = QVBoxLayout(self.page_51)
        self.verticalLayout_145.setObjectName("verticalLayout_145")
        self.textBrowser_109 = QTextBrowser(self.page_51)
        self.textBrowser_109.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_109.setObjectName("textBrowser_109")
        self.verticalLayout_145.addWidget(self.textBrowser_109)
        self.textBrowser_110 = QTextBrowser(self.page_51)
        self.textBrowser_110.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_110.setObjectName("textBrowser_110")
        self.verticalLayout_145.addWidget(self.textBrowser_110)
        self.groupBox_39 = QGroupBox(self.page_51)
        self.groupBox_39.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_39.setFlat(False)
        self.groupBox_39.setObjectName("groupBox_39")
        self.verticalLayout_146 = QVBoxLayout(self.groupBox_39)
        self.verticalLayout_146.setObjectName("verticalLayout_146")
        self.verticalLayout_147 = QVBoxLayout()
        self.verticalLayout_147.setObjectName("verticalLayout_147")
        self.radioButton_13_6 = QRadioButton(self.groupBox_39)
        self.radioButton_13_6.setStyleSheet("")
        self.radioButton_13_6.setObjectName("radioButton_13_6")
        self.verticalLayout_147.addWidget(self.radioButton_13_6)
        self.radioButton_13_7 = QRadioButton(self.groupBox_39)
        self.radioButton_13_7.setObjectName("radioButton_13_7")
        self.verticalLayout_147.addWidget(self.radioButton_13_7)
        self.radioButton_13_8 = QRadioButton(self.groupBox_39)
        self.radioButton_13_8.setObjectName("radioButton_13_8")
        self.verticalLayout_147.addWidget(self.radioButton_13_8)
        self.radioButton_13_9 = QRadioButton(self.groupBox_39)
        self.radioButton_13_9.setObjectName("radioButton_13_9")
        self.verticalLayout_147.addWidget(self.radioButton_13_9)
        self.radioButton_13_10 = QRadioButton(self.groupBox_39)
        self.radioButton_13_10.setObjectName("radioButton_13_10")
        self.verticalLayout_147.addWidget(self.radioButton_13_10)
        self.verticalLayout_146.addLayout(self.verticalLayout_147)
        self.verticalLayout_145.addWidget(self.groupBox_39)
        self.stackedWidget_4.addWidget(self.page_51)
        self.page_52 = QWidget()
        self.page_52.setObjectName("page_52")
        self.verticalLayout_148 = QVBoxLayout(self.page_52)
        self.verticalLayout_148.setObjectName("verticalLayout_148")
        self.textBrowser_111 = QTextBrowser(self.page_52)
        self.textBrowser_111.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_111.setObjectName("textBrowser_111")
        self.verticalLayout_148.addWidget(self.textBrowser_111)
        self.textBrowser_112 = QTextBrowser(self.page_52)
        self.textBrowser_112.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_112.setObjectName("textBrowser_112")
        self.verticalLayout_148.addWidget(self.textBrowser_112)
        self.groupBox_40 = QGroupBox(self.page_52)
        self.groupBox_40.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_40.setFlat(False)
        self.groupBox_40.setObjectName("groupBox_40")
        self.verticalLayout_149 = QVBoxLayout(self.groupBox_40)
        self.verticalLayout_149.setObjectName("verticalLayout_149")
        self.verticalLayout_150 = QVBoxLayout()
        self.verticalLayout_150.setObjectName("verticalLayout_150")
        self.radioButton_14_7 = QRadioButton(self.groupBox_40)
        self.radioButton_14_7.setStyleSheet("")
        self.radioButton_14_7.setObjectName("radioButton_14_7")
        self.verticalLayout_150.addWidget(self.radioButton_14_7)
        self.radioButton_14_8 = QRadioButton(self.groupBox_40)
        self.radioButton_14_8.setObjectName("radioButton_14_8")
        self.verticalLayout_150.addWidget(self.radioButton_14_8)
        self.radioButton_14_9 = QRadioButton(self.groupBox_40)
        self.radioButton_14_9.setObjectName("radioButton_14_9")
        self.verticalLayout_150.addWidget(self.radioButton_14_9)
        self.radioButton_14_10 = QRadioButton(self.groupBox_40)
        self.radioButton_14_10.setObjectName("radioButton_14_10")
        self.verticalLayout_150.addWidget(self.radioButton_14_10)
        self.radioButton_14_2 = QRadioButton(self.groupBox_40)
        self.radioButton_14_2.setObjectName("radioButton_14_2")
        self.verticalLayout_150.addWidget(self.radioButton_14_2)
        self.verticalLayout_149.addLayout(self.verticalLayout_150)
        self.verticalLayout_148.addWidget(self.groupBox_40)
        self.stackedWidget_4.addWidget(self.page_52)
        self.page_53 = QWidget()
        self.page_53.setObjectName("page_53")
        self.verticalLayout_151 = QVBoxLayout(self.page_53)
        self.verticalLayout_151.setObjectName("verticalLayout_151")
        self.textBrowser_113 = QTextBrowser(self.page_53)
        self.textBrowser_113.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_113.setObjectName("textBrowser_113")
        self.verticalLayout_151.addWidget(self.textBrowser_113)
        self.textBrowser_114 = QTextBrowser(self.page_53)
        self.textBrowser_114.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_114.setObjectName("textBrowser_114")
        self.verticalLayout_151.addWidget(self.textBrowser_114)
        self.groupBox_41 = QGroupBox(self.page_53)
        self.groupBox_41.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_41.setFlat(False)
        self.groupBox_41.setObjectName("groupBox_41")
        self.verticalLayout_152 = QVBoxLayout(self.groupBox_41)
        self.verticalLayout_152.setObjectName("verticalLayout_152")
        self.verticalLayout_153 = QVBoxLayout()
        self.verticalLayout_153.setObjectName("verticalLayout_153")
        self.radioButton_15_6 = QRadioButton(self.groupBox_41)
        self.radioButton_15_6.setStyleSheet("")
        self.radioButton_15_6.setObjectName("radioButton_15_6")
        self.verticalLayout_153.addWidget(self.radioButton_15_6)
        self.radioButton_15_7 = QRadioButton(self.groupBox_41)
        self.radioButton_15_7.setObjectName("radioButton_15_7")
        self.verticalLayout_153.addWidget(self.radioButton_15_7)
        self.radioButton_15_8 = QRadioButton(self.groupBox_41)
        self.radioButton_15_8.setObjectName("radioButton_15_8")
        self.verticalLayout_153.addWidget(self.radioButton_15_8)
        self.radioButton_15_9 = QRadioButton(self.groupBox_41)
        self.radioButton_15_9.setObjectName("radioButton_15_9")
        self.verticalLayout_153.addWidget(self.radioButton_15_9)
        self.radioButton_15_10 = QRadioButton(self.groupBox_41)
        self.radioButton_15_10.setObjectName("radioButton_15_10")
        self.verticalLayout_153.addWidget(self.radioButton_15_10)
        self.verticalLayout_152.addLayout(self.verticalLayout_153)
        self.verticalLayout_151.addWidget(self.groupBox_41)
        self.stackedWidget_4.addWidget(self.page_53)
        self.page_54 = QWidget()
        self.page_54.setObjectName("page_54")
        self.verticalLayout_154 = QVBoxLayout(self.page_54)
        self.verticalLayout_154.setObjectName("verticalLayout_154")
        self.textBrowser_115 = QTextBrowser(self.page_54)
        self.textBrowser_115.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_115.setObjectName("textBrowser_115")
        self.verticalLayout_154.addWidget(self.textBrowser_115)
        self.textBrowser_116 = QTextBrowser(self.page_54)
        self.textBrowser_116.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_116.setObjectName("textBrowser_116")
        self.verticalLayout_154.addWidget(self.textBrowser_116)
        self.groupBox_42 = QGroupBox(self.page_54)
        self.groupBox_42.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_42.setFlat(False)
        self.groupBox_42.setObjectName("groupBox_42")
        self.verticalLayout_155 = QVBoxLayout(self.groupBox_42)
        self.verticalLayout_155.setObjectName("verticalLayout_155")
        self.verticalLayout_156 = QVBoxLayout()
        self.verticalLayout_156.setObjectName("verticalLayout_156")
        self.radioButton_16_6 = QRadioButton(self.groupBox_42)
        self.radioButton_16_6.setStyleSheet("")
        self.radioButton_16_6.setObjectName("radioButton_16_6")
        self.verticalLayout_156.addWidget(self.radioButton_16_6)
        self.radioButton_16_7 = QRadioButton(self.groupBox_42)
        self.radioButton_16_7.setObjectName("radioButton_16_7")
        self.verticalLayout_156.addWidget(self.radioButton_16_7)
        self.radioButton_16_8 = QRadioButton(self.groupBox_42)
        self.radioButton_16_8.setObjectName("radioButton_16_8")
        self.verticalLayout_156.addWidget(self.radioButton_16_8)
        self.radioButton_16_9 = QRadioButton(self.groupBox_42)
        self.radioButton_16_9.setObjectName("radioButton_16_9")
        self.verticalLayout_156.addWidget(self.radioButton_16_9)
        self.radioButton_16_10 = QRadioButton(self.groupBox_42)
        self.radioButton_16_10.setObjectName("radioButton_16_10")
        self.verticalLayout_156.addWidget(self.radioButton_16_10)
        self.verticalLayout_155.addLayout(self.verticalLayout_156)
        self.verticalLayout_154.addWidget(self.groupBox_42)
        self.stackedWidget_4.addWidget(self.page_54)
        self.page_55 = QWidget()
        self.page_55.setObjectName("page_55")
        self.verticalLayout_157 = QVBoxLayout(self.page_55)
        self.verticalLayout_157.setObjectName("verticalLayout_157")
        self.textBrowser_117 = QTextBrowser(self.page_55)
        self.textBrowser_117.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_117.setObjectName("textBrowser_117")
        self.verticalLayout_157.addWidget(self.textBrowser_117)
        self.textBrowser_118 = QTextBrowser(self.page_55)
        self.textBrowser_118.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_118.setObjectName("textBrowser_118")
        self.verticalLayout_157.addWidget(self.textBrowser_118)
        self.groupBox_43 = QGroupBox(self.page_55)
        self.groupBox_43.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_43.setFlat(False)
        self.groupBox_43.setObjectName("groupBox_43")
        self.verticalLayout_158 = QVBoxLayout(self.groupBox_43)
        self.verticalLayout_158.setObjectName("verticalLayout_158")
        self.verticalLayout_159 = QVBoxLayout()
        self.verticalLayout_159.setObjectName("verticalLayout_159")
        self.radioButton_17_6 = QRadioButton(self.groupBox_43)
        self.radioButton_17_6.setStyleSheet("")
        self.radioButton_17_6.setObjectName("radioButton_17_6")
        self.verticalLayout_159.addWidget(self.radioButton_17_6)
        self.radioButton_17_7 = QRadioButton(self.groupBox_43)
        self.radioButton_17_7.setObjectName("radioButton_17_7")
        self.verticalLayout_159.addWidget(self.radioButton_17_7)
        self.radioButton_17_8 = QRadioButton(self.groupBox_43)
        self.radioButton_17_8.setObjectName("radioButton_17_8")
        self.verticalLayout_159.addWidget(self.radioButton_17_8)
        self.radioButton_17_9 = QRadioButton(self.groupBox_43)
        self.radioButton_17_9.setObjectName("radioButton_17_9")
        self.verticalLayout_159.addWidget(self.radioButton_17_9)
        self.radioButton_17_10 = QRadioButton(self.groupBox_43)
        self.radioButton_17_10.setObjectName("radioButton_17_10")
        self.verticalLayout_159.addWidget(self.radioButton_17_10)
        self.verticalLayout_158.addLayout(self.verticalLayout_159)
        self.verticalLayout_157.addWidget(self.groupBox_43)
        self.stackedWidget_4.addWidget(self.page_55)
        self.page_56 = QWidget()
        self.page_56.setObjectName("page_56")
        self.verticalLayout_160 = QVBoxLayout(self.page_56)
        self.verticalLayout_160.setObjectName("verticalLayout_160")
        self.textBrowser_119 = QTextBrowser(self.page_56)
        self.textBrowser_119.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_119.setObjectName("textBrowser_119")
        self.verticalLayout_160.addWidget(self.textBrowser_119)
        self.textBrowser_120 = QTextBrowser(self.page_56)
        self.textBrowser_120.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_120.setObjectName("textBrowser_120")
        self.verticalLayout_160.addWidget(self.textBrowser_120)
        self.groupBox_44 = QGroupBox(self.page_56)
        self.groupBox_44.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_44.setFlat(False)
        self.groupBox_44.setObjectName("groupBox_44")
        self.verticalLayout_161 = QVBoxLayout(self.groupBox_44)
        self.verticalLayout_161.setObjectName("verticalLayout_161")
        self.verticalLayout_162 = QVBoxLayout()
        self.verticalLayout_162.setObjectName("verticalLayout_162")
        self.radioButton_18_6 = QRadioButton(self.groupBox_44)
        self.radioButton_18_6.setStyleSheet("")
        self.radioButton_18_6.setObjectName("radioButton_18_6")
        self.verticalLayout_162.addWidget(self.radioButton_18_6)
        self.radioButton_18_7 = QRadioButton(self.groupBox_44)
        self.radioButton_18_7.setObjectName("radioButton_18_7")
        self.verticalLayout_162.addWidget(self.radioButton_18_7)
        self.radioButton_18_8 = QRadioButton(self.groupBox_44)
        self.radioButton_18_8.setObjectName("radioButton_18_8")
        self.verticalLayout_162.addWidget(self.radioButton_18_8)
        self.radioButton_18_9 = QRadioButton(self.groupBox_44)
        self.radioButton_18_9.setObjectName("radioButton_18_9")
        self.verticalLayout_162.addWidget(self.radioButton_18_9)
        self.radioButton_18_10 = QRadioButton(self.groupBox_44)
        self.radioButton_18_10.setObjectName("radioButton_18_10")
        self.verticalLayout_162.addWidget(self.radioButton_18_10)
        self.verticalLayout_161.addLayout(self.verticalLayout_162)
        self.verticalLayout_160.addWidget(self.groupBox_44)
        self.stackedWidget_4.addWidget(self.page_56)
        self.page_57 = QWidget()
        self.page_57.setObjectName("page_57")
        self.verticalLayout_163 = QVBoxLayout(self.page_57)
        self.verticalLayout_163.setObjectName("verticalLayout_163")
        self.textBrowser_121 = QTextBrowser(self.page_57)
        self.textBrowser_121.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_121.setObjectName("textBrowser_121")
        self.verticalLayout_163.addWidget(self.textBrowser_121)
        self.textBrowser_122 = QTextBrowser(self.page_57)
        self.textBrowser_122.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_122.setObjectName("textBrowser_122")
        self.verticalLayout_163.addWidget(self.textBrowser_122)
        self.groupBox_45 = QGroupBox(self.page_57)
        self.groupBox_45.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_45.setFlat(False)
        self.groupBox_45.setObjectName("groupBox_45")
        self.verticalLayout_164 = QVBoxLayout(self.groupBox_45)
        self.verticalLayout_164.setObjectName("verticalLayout_164")
        self.verticalLayout_165 = QVBoxLayout()
        self.verticalLayout_165.setObjectName("verticalLayout_165")
        self.radioButton_19_6 = QRadioButton(self.groupBox_45)
        self.radioButton_19_6.setStyleSheet("")
        self.radioButton_19_6.setObjectName("radioButton_19_6")
        self.verticalLayout_165.addWidget(self.radioButton_19_6)
        self.radioButton_19_7 = QRadioButton(self.groupBox_45)
        self.radioButton_19_7.setObjectName("radioButton_19_7")
        self.verticalLayout_165.addWidget(self.radioButton_19_7)
        self.radioButton_19_8 = QRadioButton(self.groupBox_45)
        self.radioButton_19_8.setObjectName("radioButton_19_8")
        self.verticalLayout_165.addWidget(self.radioButton_19_8)
        self.radioButton_19_9 = QRadioButton(self.groupBox_45)
        self.radioButton_19_9.setObjectName("radioButton_19_9")
        self.verticalLayout_165.addWidget(self.radioButton_19_9)
        self.radioButton_19_10 = QRadioButton(self.groupBox_45)
        self.radioButton_19_10.setObjectName("radioButton_19_10")
        self.verticalLayout_165.addWidget(self.radioButton_19_10)
        self.verticalLayout_164.addLayout(self.verticalLayout_165)
        self.verticalLayout_163.addWidget(self.groupBox_45)
        self.stackedWidget_4.addWidget(self.page_57)
        self.page_58 = QWidget()
        self.page_58.setObjectName("page_58")
        self.verticalLayout_166 = QVBoxLayout(self.page_58)
        self.verticalLayout_166.setObjectName("verticalLayout_166")
        self.textBrowser_123 = QTextBrowser(self.page_58)
        self.textBrowser_123.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_123.setObjectName("textBrowser_123")
        self.verticalLayout_166.addWidget(self.textBrowser_123)
        self.textBrowser_124 = QTextBrowser(self.page_58)
        self.textBrowser_124.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_124.setObjectName("textBrowser_124")
        self.verticalLayout_166.addWidget(self.textBrowser_124)
        self.groupBox_46 = QGroupBox(self.page_58)
        self.groupBox_46.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_46.setFlat(False)
        self.groupBox_46.setObjectName("groupBox_46")
        self.verticalLayout_167 = QVBoxLayout(self.groupBox_46)
        self.verticalLayout_167.setObjectName("verticalLayout_167")
        self.verticalLayout_168 = QVBoxLayout()
        self.verticalLayout_168.setObjectName("verticalLayout_168")
        self.radioButton_20_6 = QRadioButton(self.groupBox_46)
        self.radioButton_20_6.setStyleSheet("")
        self.radioButton_20_6.setObjectName("radioButton_20_6")
        self.verticalLayout_168.addWidget(self.radioButton_20_6)
        self.radioButton_20_7 = QRadioButton(self.groupBox_46)
        self.radioButton_20_7.setObjectName("radioButton_20_7")
        self.verticalLayout_168.addWidget(self.radioButton_20_7)
        self.radioButton_20_8 = QRadioButton(self.groupBox_46)
        self.radioButton_20_8.setObjectName("radioButton_20_8")
        self.verticalLayout_168.addWidget(self.radioButton_20_8)
        self.radioButton_20_9 = QRadioButton(self.groupBox_46)
        self.radioButton_20_9.setObjectName("radioButton_20_9")
        self.verticalLayout_168.addWidget(self.radioButton_20_9)
        self.radioButton_20_10 = QRadioButton(self.groupBox_46)
        self.radioButton_20_10.setObjectName("radioButton_20_10")
        self.verticalLayout_168.addWidget(self.radioButton_20_10)
        self.verticalLayout_167.addLayout(self.verticalLayout_168)
        self.verticalLayout_166.addWidget(self.groupBox_46)
        self.stackedWidget_4.addWidget(self.page_58)
        self.page_59 = QWidget()
        self.page_59.setObjectName("page_59")
        self.verticalLayout_169 = QVBoxLayout(self.page_59)
        self.verticalLayout_169.setObjectName("verticalLayout_169")
        self.textBrowser_125 = QTextBrowser(self.page_59)
        self.textBrowser_125.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_125.setObjectName("textBrowser_125")
        self.verticalLayout_169.addWidget(self.textBrowser_125)
        self.textBrowser_126 = QTextBrowser(self.page_59)
        self.textBrowser_126.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_126.setObjectName("textBrowser_126")
        self.verticalLayout_169.addWidget(self.textBrowser_126)
        self.groupBox_47 = QGroupBox(self.page_59)
        self.groupBox_47.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_47.setFlat(False)
        self.groupBox_47.setObjectName("groupBox_47")
        self.verticalLayout_170 = QVBoxLayout(self.groupBox_47)
        self.verticalLayout_170.setObjectName("verticalLayout_170")
        self.verticalLayout_171 = QVBoxLayout()
        self.verticalLayout_171.setObjectName("verticalLayout_171")
        self.radioButton_21_6 = QRadioButton(self.groupBox_47)
        self.radioButton_21_6.setStyleSheet("")
        self.radioButton_21_6.setObjectName("radioButton_21_6")
        self.verticalLayout_171.addWidget(self.radioButton_21_6)
        self.radioButton_21_7 = QRadioButton(self.groupBox_47)
        self.radioButton_21_7.setObjectName("radioButton_21_7")
        self.verticalLayout_171.addWidget(self.radioButton_21_7)
        self.radioButton_21_8 = QRadioButton(self.groupBox_47)
        self.radioButton_21_8.setObjectName("radioButton_21_8")
        self.verticalLayout_171.addWidget(self.radioButton_21_8)
        self.radioButton_21_9 = QRadioButton(self.groupBox_47)
        self.radioButton_21_9.setObjectName("radioButton_21_9")
        self.verticalLayout_171.addWidget(self.radioButton_21_9)
        self.radioButton_21_10 = QRadioButton(self.groupBox_47)
        self.radioButton_21_10.setObjectName("radioButton_21_10")
        self.verticalLayout_171.addWidget(self.radioButton_21_10)
        self.verticalLayout_170.addLayout(self.verticalLayout_171)
        self.verticalLayout_169.addWidget(self.groupBox_47)
        self.stackedWidget_4.addWidget(self.page_59)
        self.page_60 = QWidget()
        self.page_60.setObjectName("page_60")
        self.verticalLayout_172 = QVBoxLayout(self.page_60)
        self.verticalLayout_172.setObjectName("verticalLayout_172")
        self.textBrowser_127 = QTextBrowser(self.page_60)
        self.textBrowser_127.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_127.setObjectName("textBrowser_127")
        self.verticalLayout_172.addWidget(self.textBrowser_127)
        self.textBrowser_128 = QTextBrowser(self.page_60)
        self.textBrowser_128.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_128.setObjectName("textBrowser_128")
        self.verticalLayout_172.addWidget(self.textBrowser_128)
        self.groupBox_48 = QGroupBox(self.page_60)
        self.groupBox_48.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_48.setFlat(False)
        self.groupBox_48.setObjectName("groupBox_48")
        self.verticalLayout_173 = QVBoxLayout(self.groupBox_48)
        self.verticalLayout_173.setObjectName("verticalLayout_173")
        self.verticalLayout_174 = QVBoxLayout()
        self.verticalLayout_174.setObjectName("verticalLayout_174")
        self.radioButton_22_6 = QRadioButton(self.groupBox_48)
        self.radioButton_22_6.setStyleSheet("")
        self.radioButton_22_6.setObjectName("radioButton_22_6")
        self.verticalLayout_174.addWidget(self.radioButton_22_6)
        self.radioButton_22_7 = QRadioButton(self.groupBox_48)
        self.radioButton_22_7.setObjectName("radioButton_22_7")
        self.verticalLayout_174.addWidget(self.radioButton_22_7)
        self.radioButton_22_8 = QRadioButton(self.groupBox_48)
        self.radioButton_22_8.setObjectName("radioButton_22_8")
        self.verticalLayout_174.addWidget(self.radioButton_22_8)
        self.radioButton_22_9 = QRadioButton(self.groupBox_48)
        self.radioButton_22_9.setObjectName("radioButton_22_9")
        self.verticalLayout_174.addWidget(self.radioButton_22_9)
        self.radioButton_22_10 = QRadioButton(self.groupBox_48)
        self.radioButton_22_10.setObjectName("radioButton_22_10")
        self.verticalLayout_174.addWidget(self.radioButton_22_10)
        self.verticalLayout_173.addLayout(self.verticalLayout_174)
        self.verticalLayout_172.addWidget(self.groupBox_48)
        self.stackedWidget_4.addWidget(self.page_60)
        self.page_61 = QWidget()
        self.page_61.setObjectName("page_61")
        self.verticalLayout_175 = QVBoxLayout(self.page_61)
        self.verticalLayout_175.setObjectName("verticalLayout_175")
        self.textBrowser_129 = QTextBrowser(self.page_61)
        self.textBrowser_129.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_129.setObjectName("textBrowser_129")
        self.verticalLayout_175.addWidget(self.textBrowser_129)
        self.textBrowser_130 = QTextBrowser(self.page_61)
        self.textBrowser_130.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_130.setObjectName("textBrowser_130")
        self.verticalLayout_175.addWidget(self.textBrowser_130)
        self.groupBox_6 = QGroupBox(self.page_61)
        self.groupBox_6.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_176 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_176.setObjectName("verticalLayout_176")
        self.verticalLayout_177 = QVBoxLayout()
        self.verticalLayout_177.setObjectName("verticalLayout_177")
        self.radioButton_23_6 = QRadioButton(self.groupBox_6)
        self.radioButton_23_6.setStyleSheet("")
        self.radioButton_23_6.setObjectName("radioButton_23_6")
        self.verticalLayout_177.addWidget(self.radioButton_23_6)
        self.radioButton_23_7 = QRadioButton(self.groupBox_6)
        self.radioButton_23_7.setObjectName("radioButton_23_7")
        self.verticalLayout_177.addWidget(self.radioButton_23_7)
        self.radioButton_23_8 = QRadioButton(self.groupBox_6)
        self.radioButton_23_8.setObjectName("radioButton_23_8")
        self.verticalLayout_177.addWidget(self.radioButton_23_8)
        self.radioButton_23_9 = QRadioButton(self.groupBox_6)
        self.radioButton_23_9.setObjectName("radioButton_23_9")
        self.verticalLayout_177.addWidget(self.radioButton_23_9)
        self.radioButton_23_10 = QRadioButton(self.groupBox_6)
        self.radioButton_23_10.setObjectName("radioButton_23_10")
        self.verticalLayout_177.addWidget(self.radioButton_23_10)
        self.verticalLayout_176.addLayout(self.verticalLayout_177)
        self.verticalLayout_175.addWidget(self.groupBox_6)
        self.stackedWidget_4.addWidget(self.page_61)
        self.page_62 = QWidget()
        self.page_62.setObjectName("page_62")
        self.verticalLayout_178 = QVBoxLayout(self.page_62)
        self.verticalLayout_178.setObjectName("verticalLayout_178")
        self.textBrowser_131 = QTextBrowser(self.page_62)
        self.textBrowser_131.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_131.setObjectName("textBrowser_131")
        self.verticalLayout_178.addWidget(self.textBrowser_131)
        self.textBrowser_132 = QTextBrowser(self.page_62)
        self.textBrowser_132.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_132.setObjectName("textBrowser_132")
        self.verticalLayout_178.addWidget(self.textBrowser_132)
        self.groupBox_49 = QGroupBox(self.page_62)
        self.groupBox_49.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_49.setFlat(False)
        self.groupBox_49.setObjectName("groupBox_49")
        self.verticalLayout_179 = QVBoxLayout(self.groupBox_49)
        self.verticalLayout_179.setObjectName("verticalLayout_179")
        self.verticalLayout_180 = QVBoxLayout()
        self.verticalLayout_180.setObjectName("verticalLayout_180")
        self.radioButton_24_6 = QRadioButton(self.groupBox_49)
        self.radioButton_24_6.setStyleSheet("")
        self.radioButton_24_6.setObjectName("radioButton_24_6")
        self.verticalLayout_180.addWidget(self.radioButton_24_6)
        self.radioButton_24_7 = QRadioButton(self.groupBox_49)
        self.radioButton_24_7.setObjectName("radioButton_24_7")
        self.verticalLayout_180.addWidget(self.radioButton_24_7)
        self.radioButton_24_8 = QRadioButton(self.groupBox_49)
        self.radioButton_24_8.setObjectName("radioButton_24_8")
        self.verticalLayout_180.addWidget(self.radioButton_24_8)
        self.radioButton_24_9 = QRadioButton(self.groupBox_49)
        self.radioButton_24_9.setObjectName("radioButton_24_9")
        self.verticalLayout_180.addWidget(self.radioButton_24_9)
        self.radioButton_24_10 = QRadioButton(self.groupBox_49)
        self.radioButton_24_10.setObjectName("radioButton_24_10")
        self.verticalLayout_180.addWidget(self.radioButton_24_10)
        self.verticalLayout_179.addLayout(self.verticalLayout_180)
        self.verticalLayout_178.addWidget(self.groupBox_49)
        self.stackedWidget_4.addWidget(self.page_62)
        self.page_63 = QWidget()
        self.page_63.setObjectName("page_63")
        self.verticalLayout_181 = QVBoxLayout(self.page_63)
        self.verticalLayout_181.setObjectName("verticalLayout_181")
        self.textBrowser_133 = QTextBrowser(self.page_63)
        self.textBrowser_133.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_133.setObjectName("textBrowser_133")
        self.verticalLayout_181.addWidget(self.textBrowser_133)
        self.textBrowser_134 = QTextBrowser(self.page_63)
        self.textBrowser_134.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 5px;")
        self.textBrowser_134.setObjectName("textBrowser_134")
        self.verticalLayout_181.addWidget(self.textBrowser_134)
        self.groupBox_50 = QGroupBox(self.page_63)
        self.groupBox_50.setStyleSheet("QRadionButton:{\n"
"    font: 10pt \"Comic Sans MS\";\n"
"}")
        self.groupBox_50.setFlat(False)
        self.groupBox_50.setObjectName("groupBox_50")
        self.verticalLayout_182 = QVBoxLayout(self.groupBox_50)
        self.verticalLayout_182.setObjectName("verticalLayout_182")
        self.verticalLayout_183 = QVBoxLayout()
        self.verticalLayout_183.setObjectName("verticalLayout_183")
        self.radioButton_25_6 = QRadioButton(self.groupBox_50)
        self.radioButton_25_6.setStyleSheet("")
        self.radioButton_25_6.setObjectName("radioButton_25_6")
        self.verticalLayout_183.addWidget(self.radioButton_25_6)
        self.radioButton_25_7 = QRadioButton(self.groupBox_50)
        self.radioButton_25_7.setObjectName("radioButton_25_7")
        self.verticalLayout_183.addWidget(self.radioButton_25_7)
        self.radioButton_25_8 = QRadioButton(self.groupBox_50)
        self.radioButton_25_8.setObjectName("radioButton_25_8")
        self.verticalLayout_183.addWidget(self.radioButton_25_8)
        self.radioButton_25_9 = QRadioButton(self.groupBox_50)
        self.radioButton_25_9.setObjectName("radioButton_25_9")
        self.verticalLayout_183.addWidget(self.radioButton_25_9)
        self.radioButton_25_10 = QRadioButton(self.groupBox_50)
        self.radioButton_25_10.setObjectName("radioButton_25_10")
        self.verticalLayout_183.addWidget(self.radioButton_25_10)
        self.verticalLayout_182.addLayout(self.verticalLayout_183)
        self.verticalLayout_181.addWidget(self.groupBox_50)
        self.stackedWidget_4.addWidget(self.page_63)
        self.page_64 = QWidget()
        self.page_64.setObjectName("page_64")
        self.verticalLayout_184 = QVBoxLayout(self.page_64)
        self.verticalLayout_184.setObjectName("verticalLayout_184")
        self.label_21 = QLabel(self.page_64)
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius: 0px;")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_184.addWidget(self.label_21)
        self.lectComment_2 = QTextEdit(self.page_64)
        self.lectComment_2.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 5px;")
        self.lectComment_2.setObjectName("lectComment_2")
        self.verticalLayout_184.addWidget(self.lectComment_2)
        self.textBrowser_135 = QTextBrowser(self.page_64)
        self.textBrowser_135.setMinimumSize(QSize(0, 0))
        self.textBrowser_135.setMaximumSize(QSize(16777215, 80))
        self.textBrowser_135.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_135.setObjectName("textBrowser_135")
        self.verticalLayout_184.addWidget(self.textBrowser_135)
        self.recommendEdit_2 = QPlainTextEdit(self.page_64)
        self.recommendEdit_2.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius: 5px;")
        self.recommendEdit_2.setObjectName("recommendEdit_2")
        self.verticalLayout_184.addWidget(self.recommendEdit_2)
        self.stackedWidget_4.addWidget(self.page_64)
        self.page_65 = QWidget()
        self.page_65.setObjectName("page_65")
        self.verticalLayout_185 = QVBoxLayout(self.page_65)
        self.verticalLayout_185.setObjectName("verticalLayout_185")
        spacerItem33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_185.addItem(spacerItem33)
        self.submit_Btn = QPushButton(self.page_65)
        self.submit_Btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.submit_Btn.setObjectName("submit_Btn")
        self.verticalLayout_185.addWidget(self.submit_Btn)
        spacerItem34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_185.addItem(spacerItem34)
        self.stackedWidget_4.addWidget(self.page_65)
        self.verticalLayout_108.addWidget(self.stackedWidget_4)
        self.verticalLayout_106.addLayout(self.verticalLayout_108)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.prevBtn_3 = QPushButton(self.frame_9)
        self.prevBtn_3.setObjectName("prevBtn_3")
        self.horizontalLayout_10.addWidget(self.prevBtn_3)
        self.nextBtn_3 = QPushButton(self.frame_9)
        self.nextBtn_3.setObjectName("nextBtn_3")
        self.horizontalLayout_10.addWidget(self.nextBtn_3)
        self.verticalLayout_106.addLayout(self.horizontalLayout_10)
        self.verticalLayout_186.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.grading_page)
        self.available_session = QWidget()
        self.available_session.setObjectName("available_session")
        self.verticalLayout_198 = QVBoxLayout(self.available_session)
        self.verticalLayout_198.setObjectName("verticalLayout_198")
        self.frame_11 = QFrame(self.available_session)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_195 = QVBoxLayout(self.frame_11)
        self.verticalLayout_195.setObjectName("verticalLayout_195")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem35)
        self.label_22 = QLabel(self.frame_11)
        self.label_22.setText("")
        self.label_22.setPixmap(QPixmap(":/futminna_logo"))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        spacerItem36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem36)
        self.verticalLayout_195.addLayout(self.horizontalLayout_13)
        self.label_23 = QLabel(self.frame_11)
        self.label_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"padding: 3px;")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_195.addWidget(self.label_23)
        spacerItem37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem37)
        spacerItem38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem38)
        spacerItem39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem39)
        spacerItem40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem40)
        spacerItem41 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem41)
        self.goToSessionBtn = QPushButton(self.frame_11)
        self.goToSessionBtn.setObjectName("goToSessionBtn")
        self.verticalLayout_195.addWidget(self.goToSessionBtn)
        spacerItem42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_195.addItem(spacerItem42)
        self.verticalFrame_2 = QFrame(self.frame_11)
        self.verticalFrame_2.setStyleSheet("QLabel{\n"
"    padding: 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(100, 100, 100, 255));\n"
"    border-radius: 0px;\n"
"}")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_197 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_197.setObjectName("verticalLayout_197")
        spacerItem43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem43)
        spacerItem44 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem44)
        self.couseCodeLabel = QLabel(self.verticalFrame_2)
        self.couseCodeLabel.setObjectName("couseCodeLabel")
        self.verticalLayout_197.addWidget(self.couseCodeLabel)
        spacerItem45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem45)
        self.courseNameLabel = QLabel(self.verticalFrame_2)
        self.courseNameLabel.setStyleSheet("")
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.verticalLayout_197.addWidget(self.courseNameLabel)
        spacerItem46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem46)
        self.lecturerLabel = QLabel(self.verticalFrame_2)
        self.lecturerLabel.setObjectName("lecturerLabel")
        self.verticalLayout_197.addWidget(self.lecturerLabel)
        spacerItem47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem47)
        self.lectureHallLabel_2 = QLabel(self.verticalFrame_2)
        self.lectureHallLabel_2.setObjectName("lectureHallLabel_2")
        self.verticalLayout_197.addWidget(self.lectureHallLabel_2)
        spacerItem48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem48)
        spacerItem49 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem49)
        spacerItem50 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem50)
        spacerItem51 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem51)
        spacerItem52 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_197.addItem(spacerItem52)
        self.verticalLayout_195.addWidget(self.verticalFrame_2)
        self.verticalLayout_198.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.available_session)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_17.setText(_translate("MainWindow", "iLecture Grading System"))
        self.label_18.setText(_translate("MainWindow", "The efficiency of your lectures are our concern"))
        self.goto_regBtn.setText(_translate("MainWindow", "Register"))
        self.goto_loginBtn.setText(_translate("MainWindow", "Login"))
        self.forgotPassBtn.setText(_translate("MainWindow", "Forgot Password"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username:"))
        self.emailLabel.setText(_translate("MainWindow", "Student Email:"))
        self.label_2.setText(_translate("MainWindow", "Level"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Level"))
        self.comboBox.setItemText(1, _translate("MainWindow", "100Level"))
        self.comboBox.setItemText(2, _translate("MainWindow", "200Level"))
        self.comboBox.setItemText(3, _translate("MainWindow", "300Level"))
        self.comboBox.setItemText(4, _translate("MainWindow", "400Level"))
        self.comboBox.setItemText(5, _translate("MainWindow", "500Level"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.confirmPLabel.setText(_translate("MainWindow", "Confirm Password:"))
        self.regBtn.setText(_translate("MainWindow", "Register"))
        self.loginReqBtn.setText(_translate("MainWindow", "Already have an Account? Sign in"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.UsernameLabel_2.setText(_translate("MainWindow", "Username:"))
        self.passwordLabel_2.setText(_translate("MainWindow", "Password:"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.loginReqBtn_2.setText(_translate("MainWindow", "Don\'t have an Account? REGISTER"))
        self.ForgotPwordBtn.setText(_translate("MainWindow", "Forgot Password"))
        self.label_4.setText(_translate("MainWindow", "Reset Password"))
        self.label_5.setText(_translate("MainWindow", "Reset Password for"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Confirm Password:"))
        self.resetPwordBtn.setText(_translate("MainWindow", "Reset Password"))
        self.loginRetBtn.setText(_translate("MainWindow", "Return to Login Page"))
        self.label_8.setText(_translate("MainWindow", "Recover Password"))
        self.label_9.setText(_translate("MainWindow", "Enter a valid student email:"))
        self.confirmBtn.setText(_translate("MainWindow", "Confirm Email"))
        self.loginRetBtn_2.setText(_translate("MainWindow", "Return to Login Page"))
        self.label_24.setText(_translate("MainWindow", "Recover Password"))
        self.label_25.setText(_translate("MainWindow", "Enter confirmation code sent to"))
        self.label_26.setText(_translate("MainWindow", "Confirmation Code:"))
        self.confirmBtn_2.setText(_translate("MainWindow", "Confirm Email"))
        self.loginRetBtn_3.setText(_translate("MainWindow", "Return to Login Page"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/home\" /><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">Welcome to iLecture Grading System where we help achieve efficiency of lectures by grading the lecturers. To begin, click </span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-style:italic; text-decoration: underline; color:#919191;\">available sessions</span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\"> to see lectures that you can grade.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">For issues, contact our support team at:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">     </span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#dbddd8;\">iLectureGS@support.com</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "All Previous Gradings"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.availSessionBtn.setText(_translate("MainWindow", "Available Sessions"))
        self.textBrowser_136.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/home\" /><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">Welcome to iLecture Grading System where we help achieve efficiency of lectures by grading the lecturers. To begin, click</span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-style:italic; text-decoration: underline; color:#919191;\"> </span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\"> </span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-style:italic; text-decoration: underline; color:#b6b6b6;\">manage sessions</span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\"> to see lectures that you can grade.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Comic Sans MS\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">Your account has being activated as the class representative, Create sessions for others to grade, lets make our lectures efficient.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Comic Sans MS\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">For issues, contact our support team at:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">     </span><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#dbddd8;\">iLectureGS@support.com</span></p></body></html>"))
        self.manageSessionBtn.setText(_translate("MainWindow", "Manage Session"))
        self.label_14.setText(_translate("MainWindow", "Manage Sessions"))
        self.courseList.setItemText(0, _translate("MainWindow", "Select Course"))
        self.lecturerList.setItemText(0, _translate("MainWindow", "Select Lecturer"))
        self.lectHallList.setItemText(0, _translate("MainWindow", "Select Venue"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select Month"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "January"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "February"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "March"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "April"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "May"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "June"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "July"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "August"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "September"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "October"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "November"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "December"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Select Day"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_3.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_3.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_3.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_3.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_3.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_3.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_3.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_3.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_3.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_3.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_3.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_3.setItemText(31, _translate("MainWindow", "31"))
        self.timeStamp.setItemText(0, _translate("MainWindow", "AM"))
        self.timeStamp.setItemText(1, _translate("MainWindow", "PM"))
        self.createSessionBtn.setText(_translate("MainWindow", "Create Session"))
        self.closeCourseName.setText(_translate("MainWindow", "Course Name:"))
        self.closeLecturerLabel.setText(_translate("MainWindow", "Lecturer:"))
        self.lectureHallLabel.setText(_translate("MainWindow", "Lecture Hall:"))
        self.timeLabel.setText(_translate("MainWindow", "Time:"))
        self.no_students.setText(_translate("MainWindow", "No of Students Graded:"))
        self.textBrowser_137.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Comic Sans MS\'; font-size:12pt;\">If students have graded, Close the session and then upload session grading to the Admin.</span></p></body></html>"))
        self.closeSessionBtn.setText(_translate("MainWindow", "Close Session"))
        self.label_16.setText(_translate("MainWindow", "Review Grading"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">To what extend do you agree with the following statements about what this lecturer does regarding this course?</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:10pt;\">Provides students with course outlines at the beginning of each semester</span></p></body></html>"))
        self.a.setText(_translate("MainWindow", "Strongly Agree"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:10pt;\">Informs students what he/she expects from them on this course at the beginning of the semester</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:10pt;\">Provides or directs students to additional reading sources</span></p></body></html>"))
        self.d.setText(_translate("MainWindow", "TextLabel"))
        self.c.setText(_translate("MainWindow", "TextLabel"))
        self.b.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:10pt;\">Informs students about the course grading system at the beginneing of each semester</span></p></body></html>"))
        self.textBrowser_48.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.h_2.setText(_translate("MainWindow", "Strongly Disagree"))
        self.f_2.setText(_translate("MainWindow", "Strongly Agree"))
        self.textBrowser_33.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Makes the course challenging but interesting</span></p></body></html>"))
        self.e_2.setText(_translate("MainWindow", "Don\'t Know"))
        self.g_2.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_35.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is Fair with his/her grading system (marks)</span></p></body></html>"))
        self.textBrowser_30.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is tolerant of students</span></p></body></html>"))
        self.textBrowser_32.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is considerate to students</span></p></body></html>"))
        self.textBrowser_49.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Has high expectation for students</span></p></body></html>"))
        self.k_2.setText(_translate("MainWindow", "Strongly Disagree"))
        self.i.setText(_translate("MainWindow", "Strongly Disagree"))
        self.j_2.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Treats students equally regardless of gender</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Encourages students to understand all phases of the course</span></p></body></html>"))
        self.textBrowser_34.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This lecturer is accessible to students for academic Discussion</span></p></body></html>"))
        self.k.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Not available at all</span></p></body></html>"))
        self.l.setText(_translate("MainWindow", "Disagree"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Outside the classroom</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">inside the classroom</span></p></body></html>"))
        self.j.setText(_translate("MainWindow", "Agree"))
        self.textBrowser_28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">How would you rate lecturer\'s class Attendance</span></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Sometimes late to class</span></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Always late to class</span></p></body></html>"))
        self.o.setText(_translate("MainWindow", "Disagree"))
        self.n.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Does not come to class often</span></p></body></html>"))
        self.p.setText(_translate("MainWindow", "Disagree"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Always puntual to class</span></p></body></html>"))
        self.m.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.s.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Very knowledgeable of the subject matter</span></p></body></html>"))
        self.t.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Returns test grades back to students on time</span></p></body></html>"))
        self.r.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Uses variety of examples to illustrate a point</span></p></body></html>"))
        self.textBrowser_27.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Uses lecture time to tell glorifying stories</span></p></body></html>"))
        self.q.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_29.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.v.setText(_translate("MainWindow", "Strongly Agree"))
        self.textBrowser_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:9pt;\">The lecturer demands gifts from students in order to give BETTER GRADES</span></p></body></html>"))
        self.textBrowser_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:9pt;\">The lecturer demands gifts from students in order to give BETTER GRADES</span></p></body></html>"))
        self.u.setText(_translate("MainWindow", "Strongly Disagree"))
        self.w.setText(_translate("MainWindow", "Disagree"))
        self.textBrowser_23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Shows good concerns for all students</span></p></body></html>"))
        self.uploadBtn.setText(_translate("MainWindow", "Upload to Database"))
        self.discardBtn.setText(_translate("MainWindow", "Discard Grading"))
        self.prevBtn.setText(_translate("MainWindow", "Previous"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.course_code_2.setText(_translate("MainWindow", "Course Code: CPE 438"))
        self.course_2.setText(_translate("MainWindow", "Course: Assembly Language Programming"))
        self.lecturer_2.setText(_translate("MainWindow", "Lecturer: Dr. O. M Olaniyi"))
        self.lectHall_2.setText(_translate("MainWindow", "Venue: NLR 3"))
        self.textBrowser_85.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">To what extend do you agree with the following statements about what this lecturer does regarding this course?</span></p></body></html>"))
        self.textBrowser_86.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Provides students with course outlines at the beginning of each semester</span></p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_1_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_1_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_1_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_1_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_1_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_87.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">To what extend do you agree with the following statements about what this lecturer does regarding this course?</span></p></body></html>"))
        self.textBrowser_88.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Informs students about the course grading system at the beginneing of each semester</span></p></body></html>"))
        self.groupBox_28.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_2_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_2_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_2_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_2_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_2_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_89.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">To what extend do you agree with the following statements about what this lecturer does regarding this course?</span></p></body></html>"))
        self.textBrowser_90.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Informs students what he/she expects from them on this course at the beginning of the semester</span></p></body></html>"))
        self.groupBox_29.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_3_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_3_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_3_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_3_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_3_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_91.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">To what extend do you agree with the following statements about what this lecturer does regarding this course?</span></p></body></html>"))
        self.textBrowser_92.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Provides or directs students to additional reading sources</span></p></body></html>"))
        self.groupBox_30.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_4_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_4_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_4_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_4_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_4_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_93.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_94.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is considerate to students</span></p></body></html>"))
        self.groupBox_31.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_5_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_5_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_5_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_5_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_5_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_95.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_96.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is tolerant of students</span></p></body></html>"))
        self.groupBox_32.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_6_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_6_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_6_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_6_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_6_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_97.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_98.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Makes the course challenging but interesting</span></p></body></html>"))
        self.groupBox_33.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_7_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_7_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_7_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_7_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_7_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_99.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_100.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Encourages students to understand all phases of the course</span></p></body></html>"))
        self.groupBox_34.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_8_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_8_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_8_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_8_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_8_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_101.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_102.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">is Fair with his/her grading system (marks)</span></p></body></html>"))
        self.groupBox_35.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_9_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_9_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_9_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_9_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_9_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_103.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_104.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Treats students equally regardless of gender</span></p></body></html>"))
        self.groupBox_36.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_10_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_10_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_10_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_10_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_10_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_105.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This Lecturer</span></p></body></html>"))
        self.textBrowser_106.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Has high expectation for students</span></p></body></html>"))
        self.groupBox_37.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_11_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_11_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_11_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_11_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_11_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_107.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This lecturer is accessible to students for academic Discussion</span></p></body></html>"))
        self.textBrowser_108.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">inside the classroom</span></p></body></html>"))
        self.groupBox_38.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_12_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_12_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_12_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_12_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_12_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_109.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This lecturer is accessible to students for academic Discussion</span></p></body></html>"))
        self.textBrowser_110.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Outside the classroom</span></p></body></html>"))
        self.groupBox_39.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_13_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_13_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_13_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_13_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_13_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_111.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">This lecturer is accessible to students for academic Discussion</span></p></body></html>"))
        self.textBrowser_112.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Not available at all</span></p></body></html>"))
        self.groupBox_40.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_14_7.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_14_8.setText(_translate("MainWindow", "Agree"))
        self.radioButton_14_9.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_14_10.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_14_2.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_113.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">How would you rate lecturer\'s class Attendance</span></p></body></html>"))
        self.textBrowser_114.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Always puntual to class</span></p></body></html>"))
        self.groupBox_41.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_15_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_15_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_15_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_15_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_15_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_115.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">How would you rate lecturer\'s class Attendance</span></p></body></html>"))
        self.textBrowser_116.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Always late to class</span></p></body></html>"))
        self.groupBox_42.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_16_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_16_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_16_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_16_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_16_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_117.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">How would you rate lecturer\'s class Attendance</span></p></body></html>"))
        self.textBrowser_118.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Sometimes late to class</span></p></body></html>"))
        self.groupBox_43.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_17_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_17_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_17_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_17_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_17_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_119.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">How would you rate lecturer\'s class Attendance</span></p></body></html>"))
        self.textBrowser_120.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Does not come to class often</span></p></body></html>"))
        self.groupBox_44.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_18_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_18_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_18_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_18_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_18_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_121.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_122.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Uses lecture time to tell glorifying stories</span></p></body></html>"))
        self.groupBox_45.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_19_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_19_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_19_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_19_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_19_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_123.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_124.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Very knowledgeable of the subject matter</span></p></body></html>"))
        self.groupBox_46.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_20_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_20_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_20_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_20_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_20_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_125.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_126.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Uses variety of examples to illustrate a point</span></p></body></html>"))
        self.groupBox_47.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_21_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_21_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_21_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_21_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_21_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_127.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_128.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Returns test grades back to students on time</span></p></body></html>"))
        self.groupBox_48.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_22_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_22_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_22_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_22_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_22_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_129.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_130.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">Shows good concerns for all students</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_23_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_23_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_23_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_23_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_23_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_131.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_132.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">The lecturer demands gifts from students in order to give BETTER GRADES</span></p></body></html>"))
        self.groupBox_49.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_24_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_24_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_24_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_24_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_24_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.textBrowser_133.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:12pt;\">Lecturer\'s Overall Effort for this course</span></p></body></html>"))
        self.textBrowser_134.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">uses some modern technologies in teaching (projectors, power points and other audio Visual)</span></p></body></html>"))
        self.groupBox_50.setTitle(_translate("MainWindow", "Options"))
        self.radioButton_25_6.setText(_translate("MainWindow", "Strongly Agree"))
        self.radioButton_25_7.setText(_translate("MainWindow", "Agree"))
        self.radioButton_25_8.setText(_translate("MainWindow", "Do not Know"))
        self.radioButton_25_9.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_25_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_21.setText(_translate("MainWindow", "COMMENT FREELY ON THE COURSE AND THE LECTURER"))
        self.textBrowser_135.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'consolas\'; font-size:11pt;\">MAKE SUGGESTIONS ON WAYS OF IMPROVING THE DELIVERY OF THE COURSE</span></p></body></html>"))
        self.submit_Btn.setText(_translate("MainWindow", "Submit"))
        self.prevBtn_3.setText(_translate("MainWindow", "Previous"))
        self.nextBtn_3.setText(_translate("MainWindow", "Next"))
        self.label_23.setText(_translate("MainWindow", "Available Sessions"))
        self.goToSessionBtn.setText(_translate("MainWindow", "Click to go to Session"))
        self.couseCodeLabel.setText(_translate("MainWindow", "CPE 438"))
        self.courseNameLabel.setText(_translate("MainWindow", "Study Of Assembly Language Programmming"))
        self.lecturerLabel.setText(_translate("MainWindow", "Dr. O. M. Olaniyi"))
        self.lectureHallLabel_2.setText(_translate("MainWindow", "NLR Room 3"))
        self.nextBtn_3.clicked.connect(self.nextGradePage)
        self.nextBtn.clicked.connect(self.nextReviewPage)
        self.prevBtn_3.clicked.connect(self.prevGradePage)
        self.prevBtn.clicked.connect(self.prevReviewPage)
        self.btnGroup1 = QButtonGroup()
        self.btnGroup2 = QButtonGroup()
        self.btnGroup3 = QButtonGroup()
        self.btnGroup4 = QButtonGroup()
        self.btnGroup5 = QButtonGroup()
        self.btnGroup6 = QButtonGroup()
        self.btnGroup7 = QButtonGroup()
        self.btnGroup8 = QButtonGroup()
        self.btnGroup9 = QButtonGroup()
        self.btnGroup10 = QButtonGroup()
        self.btnGroup11 = QButtonGroup()
        self.btnGroup12 = QButtonGroup()
        self.btnGroup13 = QButtonGroup()
        self.btnGroup14 = QButtonGroup()
        self.btnGroup15 = QButtonGroup()
        self.btnGroup16 = QButtonGroup()
        self.btnGroup17 = QButtonGroup()
        self.btnGroup18 = QButtonGroup()
        self.btnGroup19 = QButtonGroup()
        self.btnGroup20 = QButtonGroup()
        self.btnGroup21 = QButtonGroup()
        self.btnGroup22 = QButtonGroup()
        self.btnGroup23 = QButtonGroup()
        self.btnGroup24 = QButtonGroup()
        self.btnGroup25 = QButtonGroup()
        self.createButtonGroups()
        self.submit_Btn.clicked.connect(self.getGrade)

    def nextGradePage(self):
        self.nextPage(self.stackedWidget_4, 26)

    def prevGradePage(self):
        self.prevPage(self.stackedWidget_4)

    def nextPage(self, widget, limit):
        i = widget.currentIndex()
        if i < limit:
            i += 1
            widget.setCurrentIndex(i)

    def prevPage(self, widget, limit = 0):
        i = widget.currentIndex()
        if i > limit:
            i -= 1
            widget.setCurrentIndex(i)

    def prevReviewPage(self):
        self.prevPage(self.stackedWidget_2)

    def nextReviewPage(self):
        self.nextPage(self.stackedWidget_2, 7)

    def createButtonGroups(self):
        btnGroups = [
                self.btnGroup1, self.btnGroup2, self.btnGroup3, self.btnGroup4, self.btnGroup5, self.btnGroup6,
                self.btnGroup7, self.btnGroup8, self.btnGroup9, self.btnGroup10, self.btnGroup11, self.btnGroup12,
                self.btnGroup13, self.btnGroup14, self.btnGroup15, self.btnGroup16, self.btnGroup17, self.btnGroup18,
                self.btnGroup19, self.btnGroup20, self.btnGroup21, self.btnGroup22, self.btnGroup23, self.btnGroup24, 
                self.btnGroup25
                ]
        for i in range(len(btnGroups)):
            btnGroups[i].setObjectName("btnGroup{0}".format(i+1))

        grade = ["Strongly Disagree", "Disagree", "Don't Know", "Agree", "Strongly Agree"]
        j = len(btnGroups) - 1
        k = 5
        x = self.stackedWidget_4.findChildren(QVBoxLayout)
        for layout in x:
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, QRadioButton):
                    # print(widget.text(), k)
                    btnGroups[j].addButton(widget)
                    btnGroups[j].setId(widget, k)
                    k -= 1
                    if widget.text() == "Do not Know":
                        widget.setChecked(True)
                    if k <= 0:
                        k = 5
                        j -= 1
                        break

    def getGrade(self):
        grade = [
                self.btnGroup1.checkedId(), self.btnGroup2.checkedId(), self.btnGroup3.checkedId(), self.btnGroup4.checkedId(), self.btnGroup5.checkedId(),
                self.btnGroup6.checkedId(), self.btnGroup7.checkedId(), self.btnGroup8.checkedId(), self.btnGroup9.checkedId(), self.btnGroup10.checkedId(),
                self.btnGroup11.checkedId(), self.btnGroup12.checkedId(), self.btnGroup13.checkedId(), self.btnGroup14.checkedId(), self.btnGroup15.checkedId(),
                self.btnGroup16.checkedId(), self.btnGroup17.checkedId(), self.btnGroup18.checkedId(), self.btnGroup19.checkedId(), self.btnGroup20.checkedId(),
                self.btnGroup21.checkedId(), self.btnGroup22.checkedId(), self.btnGroup23.checkedId(), self.btnGroup24.checkedId(), self.btnGroup25.checkedId()
                ]
        lectComment = self.lectComment_2.toPlainText()
        recommendations = self.recommendEdit_2.toPlainText()
        return grade, lectComment, recommendations

    # def populateMenu()
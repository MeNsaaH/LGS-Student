from display import Display
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class View(Display):
    """docstring for View"""
    def __init__(self, parent = None):
        # super(View, self).__init__(parent)
        self.setupUi(parent)
        self.visible = False
        self.hideMenu()
        self.menu_manageSessionBtn.hide()
        self.menu_ReviewSessionBtn.hide()
        self.menu_logoutBtn.hide()
        self.menu_availSessionBtn.hide()
        self.menuBtn.clicked.connect(self.showMenu)
        self.nextBtn_3.clicked.connect(self.nextGradePage)
        self.prevBtn_3.clicked.connect(self.prevGradePage)
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

    def showMenu(self):
        if not self.menuVisible:
            icon = QIcon()
            icon.addPixmap(QPixmap(":/menu_close"), QIcon.Normal, QIcon.Off)
            self.menuBtn.setIcon(icon)
            self.menuBtn.setIconSize(QSize(40, 19))
            self.frame_13.show()
            self.menuVisible = True
        else:
            self.hideMenu()
            

    def hideMenu(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/menu"), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(40, 19))
        self.frame_13.hide()
        self.menuVisible = False

    def populateMenu(self, cr = False):
        self.menu_loginBtn.hide()
        self.menu_regBtn.hide()
        self.menu_recPassBtn.hide()
        if cr:
            self.menu_manageSessionBtn.show()
            self.menu_ReviewSessionBtn.show()
        else:
            self.menu_availSessionBtn.show()
        self.menu_logoutBtn.show()

    def populateLogoutMenu(self):
        self.menu_manageSessionBtn.hide()
        self.menu_ReviewSessionBtn.hide()
        self.menu_availSessionBtn.hide()
        self.menu_logoutBtn.hide()
        self.menu_loginBtn.show()
        self.menu_regBtn.show()
        self.menu_recPassBtn.show()
        self.hideMenu()
            
    def resizeWindow(self, width, height):
        self.scrollArea.setGeometry(0, 0, width, height)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(int(width - (5*width)/100)/2)
        
#import system files
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#import view files
from view import View
import qrc_resource

#import model files
from authe import Auth


class App(QMainWindow):
    """Controls the application logic of the Students end"""
    resized = pyqtSignal()
    user = {"loggedIn": False, "cr": False}

    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)

        #instantiate the general Display 
        self.disp = View(self)
        self.auth = Auth(self)
        self.resized.connect(self.resizeWindow)
        self.setMinimumSize(494, 300)

        self.setWindowIcon(QIcon(':/futminna_logo'))
        self.setWindowTitle('iLecture Grading System')
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.disp.goto_regBtn.clicked.connect(self.gotoRegister)
        self.disp.goto_loginBtn.clicked.connect(self.gotoLogin)
        self.disp.loginReqBtn_2.clicked.connect(self.gotoRegister)
        self.disp.loginReqBtn.clicked.connect(self.gotoLogin)
        self.disp.loginRetBtn.clicked.connect(self.gotoLogin)
        self.disp.loginRetBtn_2.clicked.connect(self.gotoLogin)
        self.disp.loginRetBtn_3.clicked.connect(self.gotoLogin)
        self.disp.forgotPassBtn.clicked.connect(self.gotoFGP)
        self.disp.ForgotPwordBtn.clicked.connect(self.gotoFGP)
        self.disp.regBtn.clicked.connect(self.addUser)
        self.disp.loginBtn.clicked.connect(self.login)
        self.disp.confirmBtn.clicked.connect(self.check_email)
        self.disp.confirmBtn_2.clicked.connect(self.confirmUser)
        self.disp.resetPwordBtn.clicked.connect(self.pwordReset)
        self.disp.goToSessionBtn.clicked.connect(self.gotoGrade)
        self.disp.submit_Btn.clicked.connect(self.uploadGrade)
        self.disp.availSessionBtn.clicked.connect(self.sessions)
        self.disp.manageSessionBtn.clicked.connect(self.processSession)
        self.disp.closeSessionBtn.clicked.connect(self.closeSession)
        self.disp.createSessionBtn.clicked.connect(self.createSession)
        self.disp.uploadBtn.clicked.connect(self.crUploadGrade)
        self.disp.discardBtn.clicked.connect(self.crDiscardGrade)
        self.disp.menu_homeBtn.clicked.connect(self.gotoHome)
        self.disp.menu_loginBtn.clicked.connect(self.gotoLogin)
        self.disp.menu_regBtn.clicked.connect(self.gotoRegister)
        self.disp.menu_recPassBtn.clicked.connect(self.gotoFGP)
        self.disp.menu_manageSessionBtn.clicked.connect(self.processSession)
        self.disp.menu_ReviewSessionBtn.clicked.connect(self.reviewSession)
        self.disp.menu_availSessionBtn.clicked.connect(self.sessions)
        self.disp.menu_logoutBtn.clicked.connect(self.logout)
        self.disp.stackedWidget.currentChanged.connect(self.disp.hideMenu)
  
    def gotoRegister(self):
        self.disp.usernameLineEdit.clear()
        self.disp.emailEdit.clear()
        self.disp.passwordEdit.clear()
        self.disp.confirmPLabel_2.clear()
        self.disp.comboBox.setCurrentIndex(0)
        if self.user["loggedIn"]:
            self.gotoHome()
        self.disp.stackedWidget.setCurrentIndex(1)
    
    def gotoLogin(self):
        if self.user["loggedIn"]:
            self.gotoHome()
        self.disp.stackedWidget.setCurrentIndex(2)

    def gotoFGP(self):
        self.disp.pword.clear()
        self.disp.confirmPword.clear()
        self.disp.confirmEmail.clear()
        self.disp.confirmEmail_2.clear()
        if self.user["loggedIn"]:
            self.gotoHome()
        self.disp.stackedWidget.setCurrentIndex(4)
        
    def gotoGrade(self):
        self.disp.stackedWidget.setCurrentIndex(10)
        
    def gotoHome(self):
        #use session variables to check which home to go to
        try:
            if self.user["loggedIn"]:
                if self.user["cr"]:
                    #goto Class Rep Home page
                    self.disp.stackedWidget.setCurrentIndex(7)
                    pass
                else:
                    #goto Student Home Page
                    self.disp.stackedWidget.setCurrentIndex(6)
                    pass
            else:
                self.disp.stackedWidget.setCurrentIndex(0)
        except Exception as e:
            raise(e)
            
    def addUser(self):
        if self.disp.comboBox.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Select a level")
            return
        self.user = {
                    "username": self.disp.usernameLineEdit.text(),
                    "email": self.disp.emailEdit.text(),
                    "level": int(self.disp.comboBox.currentText()[:3]),
                    "password":self.disp.passwordEdit.text(), 
                    "confirmP": self.disp.confirmPLabel_2.text()
                    }
        self.auth.addUser(self.user, self.disp)
    
    def login(self):
        self.auth.login(self.disp)
        self.populateLists()
        
    def check_email(self):
        self.auth.check_email(self.disp)
    
    def confirmUser(self):
        self.auth.confirmUser(self.disp)
    
    def pwordReset(self):
        self.auth.pwordReset(self.disp)
    
    def sessions(self):
        self.disp.courseList.setCurrentIndex(0)
        self.disp.lecturerList.setCurrentIndex(0)
        self.disp.lectHallList.setCurrentIndex(0)
        self.disp.comboBox_2.setCurrentIndex(0)
        self.disp.comboBox_3.setCurrentIndex(0)

        err, session = self.auth.checkSession(self.disp)
        if session is not None:
            self.disp.goToSessionBtn.setText("Click to continue to Session")
            self.disp.couseCodeLabel.setText("<b>Course Code</b>: " + session["course_code"])
            self.disp.courseNameLabel.setText("<b>Course: </b>" + session["desc"])
            self.disp.lecturerLabel.setText("<b>Lecturer: </b>" + session["lecturer"])
            self.disp.lectureHallLabel_2.setText("<b>Venue: </b>" + session["lecture_env"])
            self.disp.course_code_2.setText("Course Code: " + session["course_code"])
            self.disp.course_2.setText("Course: " + session["desc"])
            self.disp.lecturer_2.setText("Lecturer: " + session["lecturer"])
            self.disp.lectHall_2.setText("Lecture Venue: " + session["lecture_env"])
        else:
            self.disp.goToSessionBtn.setText("No Available Session")
            self.disp.goToSessionBtn.setEnabled(False)

        if err == 1:
            self.disp.goToSessionBtn.setEnabled(False)
            self.disp.goToSessionBtn.setText("No Longer Available")
        if err == 0:
            self.disp.goToSessionBtn.setEnabled(True)
        self.disp.stackedWidget.setCurrentIndex(11)

    def uploadGrade(self):
        self.auth.uploadGrade(self.disp)

    def processSession(self):
        x, y = self.auth.manageSession(self.disp)
        if x:
            self.disp.stackedWidget_5.setCurrentIndex(y)
            self.disp.createSessionBtn.setEnabled(True)
            self.disp.label.setText("Manage Session")
        else:
            self.disp.stackedWidget_5.setCurrentIndex(y)
            self.disp.createSessionBtn.setEnabled(False)
            self.disp.label_14.setText("Failed To load Session Info")
        self.disp.stackedWidget.setCurrentIndex(8)
    
    def closeSession(self):
        self.auth.closeSession(self.disp)

    def createSession(self):
        self.auth.createSession(self.disp)

    def populateLists(self):
        env, lect, cous = self.auth.fullDetails
        
        if env:
            lect_env = []
            lecturers = []
            courses = []
            for i in env:
                lect_env.append(i[1])
            for j in lect:
                lecturers.append(j[1] + '. ' + j[2])
            for x in cous:
                courses.append(x[0] + ' - ' + x[1])
            self.disp.lectHallList.addItems(lect_env)
            self.disp.lecturerList.addItems(lecturers)
            self.disp.courseList.addItems(courses)
            self.disp.label_14.setText("Manage Session")
        else:
            self.disp.label_14.setText("Failed to Load Departmental Data, Try Again Later")

    def reviewSession(self):
        self.auth.reviewSession(self.disp)

    def crUploadGrade(self):
        self.auth.crUploadGrade(self.disp)

    def crDiscardGrade(self):
        self.auth.crDiscardGrade(self.disp)
    
    def logout(self):
        self.user.clear()
        self.user["loggedIn"] = False
        self.user["cr"] = False
        self.disp.populateLogoutMenu()
        self.disp.stackedWidget.setCurrentIndex(0)
        self.auth.reset()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(App, self).resizeEvent(event)

    def resizeWindow(self):
        self.disp.resizeWindow(self.width(), self.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName("iLectureGS.org")
    app.setApplicationName("iLecture Grading System")
    app.setWindowIcon(QIcon(":/futminna_logo"))
    a = App()
    a.show()
    app.exec_()
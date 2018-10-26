import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from smtplib import SMTP
from email.mime.text import MIMEText
from email.parser import BytesParser, Parser
from email.policy import default
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

from database import Database
from Validator import Validator
from exceptions import *


class Auth(QObject):
    """
    Authenticates an email
    """  

    fullDetails = (None, None, None)
    DB_NAME = "../LectureGS.db"
    user = dict()
    cr_data = dict()

    def __init__(self, parent):
        super(Auth, self).__init__(parent)
        self.db = Database(self.DB_NAME)
        self.val = Validator()
        self.home = parent
        self.grade_indices = [i for i in ascii_lowercase][:-1]

    def genCode(self, codeLen):
        code = ''.join(choice(ascii_uppercase + digits +ascii_lowercase) for _ in range(codeLen))
        return code

    def sendMsg(self, email, subject, body):
        headers = Parser(policy=default).parsestr(
                    "From: iLecture Grading System <ilgs.support.com>\n"
                    "To: <{0}>\n"
                    "Subject: {1}\n"
                    "\n{2}\nIf you did not register for this, kindly ignore this message".format(email, subject, body))
        try:
            # print(headers)
            server = SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("mmadumanasseh@gmail.com", "bravo9090")
            server.send_message(headers)
            server.quit()
            return True

        except Exception:
            # print (e)
            return False

    def updateUserStatus(self, username, token, password):
        try:
            a = self.db.userExists([username], ["username"], "Token")
            if not a[0]:
                return self.db.addRow("Token", ["token", "username", "password"], [token, username, password])
            else:
                return self.db.updateField(["token"], [token], "Token", username)
        except Exception:
            return False, "Could not Verify username, try again later"
        
    def sendToken(self, email, username, password=0):
        try:
            token = self.genCode(10)
            msg = "use this code to Verify your account email\n"\
                "Code: {0}".format(token)
            self.sendMsg(email, "Confirm Your Email Address", msg)
            return self.updateUserStatus(username, token, password)
        except Exception:
            # print(e)
            return False, "Could not Connect to database, try again later", token

    def confirmCode(self, username, code):
        try:
            status, data = self.db.getRow("Token", ["username"], [username])
            if status and len(data)>0:
                if code.strip() == data["token"] and int(data["password"]) == 0:
                    if self.db.updateField(["status"], [1], "Students", username)[0]:
                        if self.db.deleteRow("Token", ["username"], [username]):
                            return True, 0
                if code.strip() == data["token"] and int(data["password"]) == 1:
                    return True, 1
            return False, data
        except Exception:
            # print(e)
            return False, "Could not Verify, try again later"

    def isClassRep(self, s_id):
        return self.db.userExists([s_id], ["student_id"], "ClassReps")

    def isValidEmail(self, email):
        return self.db.userExists([email], ["email"], "Students")

    def resetPassword(self, password, confirmP, username):
        try:
            if self.db.resetPassword(password, confirmP, username)[0]:
                return self.db.deleteRow("Token", ["username"], [username])
            return self.db.resetPassword(password, confirmP, username)[0]
        except Exception:
            return False, "Error Resetting Password, try again later"

    def addUser(self, user, disp):
        '''
        Adds a user to the database upon clicking the register button
        '''
        parent = self.home
        self.user = user
        try:
            n = self.db.registerUser(self.user, commit=False)
            if n[0]:
                QMessageBox.information(parent, "Success", "Your Registration was successful\n"\
                                                "Confirm Your email Address to proceed to using the application ")
                send_token = self.sendToken(self.user["email"], self.user["username"])
                if send_token[0]:
                    disp.label_25.setText("Enter code sent to {0}".format(self.user["email"]))
                    disp.label_24.setText("Confirm Your Email Address")
                else:
                    raise RegistrationError(send_token[1])
                    
            else:
                raise RegistrationError(n[1])
        except RegistrationError:
            # tb = sys.exc_info()[1]
            # print(tb)
            # print(e)
            QMessageBox.critical(parent, "Error", "Registration could not be completed, Check your connection and try again later", QMessageBox.Ok)
        else:
            self.db.save()
            disp.stackedWidget.setCurrentIndex(5)

    def login(self, this):
        '''
        logs the user in upon clicking the login button
        '''
        try:
            u_email = (this.UsernameLineEdit.text()).lower()
            password = this.PasswordEdit.text()
            status, user = self.db.login(u_email, password)
            if status:
                #check if user is on token table and redirect to confirm page
                self.user = user
                if int(user["status"]) != 1:
                    #redirect to complete registration
                    this.label_25.setText("Enter code sent to {0}".format(self.user["email"]))
                    this.label_24.setText("Confirm Your Email Address")
                    this.stackedWidget.setCurrentIndex(5)
                else:
                    x, self.cr_data = self.isClassRep(self.user["id"])

                    if x:
                        this.populateMenu(cr = True)
                        self.home.user["cr"] =  True
                        this.stackedWidget.setCurrentIndex(7)
                        self.fullDetails = self.getFullDetails()
                        # print("Full Details", self.fullDetails)
                    else:
                        this.populateMenu(cr = False)
                        self.loadPreviousGrades(this)
                        self.home.user["cr"] = False
                        this.stackedWidget.setCurrentIndex(6)
                self.home.user["loggedIn"] = True
            else:
                raise LoginError
                
        except LoginError:
            QMessageBox.critical(self.home, "Error", "Invalid User details", QMessageBox.Ok)
        except Exception:
            # print(e)
            QMessageBox.warning(self.home, "Error", "an unexpected error, try again later")

    def check_email(self, this):
        email = (this.confirmEmail.text()).lower()
        x, error = self.isValidEmail(email)
        
        if x:
            s = self.sendToken(email, error["username"], 1)
            if s[0]:
                this.label_25.setText("Enter code sent to {0}".format(email))
                self.user["username"] = error["username"]
                this.stackedWidget.setCurrentIndex(5)
            else:
                QMessageBox.warning(self.home, "Error", "Could not send confirmation code, try again later", QMessageBox.Ok)
        else:
            QMessageBox.critical(self.home, "Error", error, QMessageBox.Ok)

    def confirmUser(self, this):
        code = this.confirmEmail_2.text()
        a, x = self.confirmCode(self.user["username"], code)
        # # print(a, x)
        if a:
            if x == 0:
                # # print("registration passed")
                QMessageBox.information(self.home, "Success", "Account has being verified, You can now use grading services. Login to continue")
                '''
                Check if user is a student or a class rep
                '''
                self.home.logout()
                this.stackedWidget.setCurrentIndex(2)
            if x == 1:
                # # print("password can then be reset")
                this.label_5.setText("Reset password for <i><b><u>{0}'s</u></b></i> account".format(self.user["username"]))
                this.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.critical(self.home, "Error", "Code does not match confirmation code", QMessageBox.Ok)

    def pwordReset(self, this):
        password = this.pword.text()
        confirmP = this.confirmPword.text()
        if self.resetPassword(password, confirmP, self.user["username"])[0]:
            QMessageBox.information(self.home, "Success", "Your password has being reset\n" 
                                    "You can now login with your new password")
            this.stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.critical(self.home, "Error", self.resetPassword(password, confirmP, self.user["username"])[1])

    def getPreviousGrades(self, id):
        previousGrades = self.db.getRow("Gradings", ["student_id"], [id])
        return previousGrades

    def loadPreviousGrades(self, this):
        stat, self.previousGrades = self.getPreviousGrades(self.user["id"])
        if stat:
            if len(self.previousGrades) >=  1:
                try:
                    this.tableWidget.setRowCount(len(list(self.previousGrades.values())[0]))
                except Exception as e:
                    this.tableWidget.setRowCount(1)
            this.tableWidget.setAlternatingRowColors(True)
            this.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            this.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            this.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
            item, col = None, None
            try:
                row = len(list(self.previousGrades.values())[0]) - 1
            except Exception as e:
                # print(e)
                row = 0
            print(row)
            try:        
                l = row
                for i in self.previousGrades:

                    for x in self.previousGrades[i]:
                        avail = False
                        if i == "course_code":
                            item = QTableWidgetItem('{0}'.format(x))
                            col = 0
                            avail = True
                            
                        if i == 'time':
                            item = QTableWidgetItem('{0}'.format(x))
                            col = 1
                            avail = True
                        if avail:
                            this.tableWidget.setItem(row, col, item)
                            row -= 1
                    row = l
        
            except Exception as e:
                print(e)
                item = QTableWidgetItem(list(self.previousGrades.values())[3])
                this.tableWidget.setItem(row, 0, item)
                item = QTableWidgetItem(list(self.previousGrades.values())[4])
                this.tableWidget.setItem(row, 1, item)

    def checkSession(self, this):
        x, session = self.db.getRow("ClassReps", ["level"], [self.user['level']])
        #if session is on
        self.session_details = None
        error = None
        try:
            if x and int(session['session_start']) == 1:
                i, lecturer_details = self.db.getRow("Lecturers", ["id"], [session["lecturer_id"]])
                j, lecture_env = self.db.getRow("LectureEnv", ["id"], [session["lecture_env_id"]])
                l, course_details = self.db.getRow("Courses", ['course_code'], [session['course_code']])
                
                self.session_details = session

                self.session_details["lecturer"] = lecturer_details["title"] + "." + lecturer_details["fname"]
                self.session_details["lecture_env"] = lecture_env["description"]
                self.session_details['desc'] = course_details["description"]
                
                if int(self.user["grade_check"]) == 1:
                    error = 1
                else:
                    error = 0
        except Exception as e:
            print("Error: " + e)
        finally:
            return error, self.session_details

    def uploadGrade(self, obj):
        values = [self.session_details["rating_id"], self.user["id"], self.session_details["course_code"], self.session_details["time"],
                self.session_details["lecturer_id"], self.session_details["lecture_env_id"]]
        fields = ["rating_id", "student_id", "course_code", "time", "lecturer_id", "lecture_env_id"]

        grade, lectComment, recmmd = obj.getGrade()
        for i, x in enumerate(grade):
            grade[i] = int(x) - 3
            

        grade.append(lectComment)
        grade.append(recmmd)
        field = self.grade_indices
        field.append("lectComment")
        field.append("recommendations")
        values += grade
        fields += field
        

        if(self.db.addRow("Gradings", fields, values))[0]:
            if self.db.updateField(["rating_id", "grade_check"], [self.session_details["rating_id"], 0], "Students", self.user["username"])[0]:
                QMessageBox.information(self.home, "Success", "You have succefully graded your lecture {0}".format(self.session_details["course_code"]), QMessageBox.Ok)
                self.user["grade_check"] = 1
                self.loadPreviousGrades(obj)
                self.home.gotoHome()
                

    def manageSession(self, obj):
        ss = (False, False)
        try:
            # print(self.cr_data["session_start"])
            if int(self.cr_data["session_start"]) == 1:
                i, self.session_lect_details = self.db.getRow("Lecturers", ["id"], [self.cr_data["lecturer_id"]])
                j, self.session_lecture_env = self.db.getRow("LectureEnv", ["id"], [self.cr_data["lecture_env_id"]])
                obj.closeCourseName.setText("<b>Course:</b> <i>{0}</i>".format(self.cr_data["course_code"]))
                obj.closeLecturerLabel.setText("<b>Lecturer:</b> <i>{0}. {1}</i>".format(self.session_lect_details["title"], self.session_lect_details["fname"]))
                obj.lectureHallLabel.setText("<b>Venue:</b> <i>{0}</i>".format(self.session_lecture_env["description"]))
                obj.timeLabel.setText("<b>Time:</b> <i>{0}</i>".format(self.cr_data["time"]))
                x, self.allGrades = self.db.getRows('Gradings', ["id"], ['rating_id'], [self.cr_data['rating_id']], withWhere = True)
                if x:
                    obj.no_students.setText("<b>No of Students Graded:</b> <i>{0}</i>".format(len(self.allGrades)))
                ss = (True, 1)
            else:
                ss = (True, 0)
        except Exception as e:
            # print(e)
            raise(e)
            
        finally:
            return ss

    def closeSession(self, obj):
        QMessageBox.question(self.home, "Close Session", "Are you sure you want to close session?")
        try:
            if QMessageBox.Yes:
                
                if (self.db.updateField(['session_start'], [0], "ClassReps", self.user["id"], 'student_id')[0]) and (self.db.updateField(['review'], [1], "ClassReps", self.user["id"], 'student_id')[0]):

                    self.cr_data["session_start"] = 0
                    self.cr_data["review"] = 1
                    obj.closeCourseName.setText("Course: ")
                    obj.closeLecturerLabel.setText("Lecturer: ")
                    obj.lectureHallLabel.setText("Venue: ")
                    obj.timeLabel.setText("Time: ")   
                    QMessageBox.information(self.home, "Success", "Session Closed successfully")   
                    obj.stackedWidget.setCurrentIndex(7)          
        except Exception as e:
            # print(e)
            return False

    def createSession(self, obj):
        error = None
        x, err = self.val.validateDate(obj.comboBox_3.currentIndex(), obj.comboBox_2.currentIndex(), obj.spinBox.value())
        if not x:
            error = err
        if obj.courseList.currentIndex() == 0:
            error = "Select Course"
        if obj.lectHallList.currentIndex() == 0:
            error = "Select Lecture Venue"
        if obj.lecturerList.currentIndex() == 0:
            error = "Select Lecturer"
        if error is not None:
            QMessageBox.critical(self.home, "Error", error)
            return False

        course, course_desc = self.courses[obj.courseList.currentIndex() - 1]
        lect_env = self.lecture_env[obj.lectHallList.currentIndex() - 1][0]
        lecturer = self.lect_details[obj.lecturerList.currentIndex() - 1][0]
        date = [obj.comboBox_2.currentIndex(), obj.comboBox_3.currentIndex(), obj.spinBox.value()]
        time = str(obj.timeSpinBox.value()) + ' ' + obj.timeStamp.currentText() + ' ' + obj.comboBox_3.currentText() + ', '  + obj.comboBox_2.currentText() + ' ' + obj.comboBox_3.currentText() + ', ' + str(obj.spinBox.value())

        try:
            if '_' in self.cr_data["rating_id"]:
                x = '_' + str(int(self.cr_data["rating_id"].split("_")[1]) + 1)
            else:
                x = '_00'
            rating_id = str(self.cr_data["level"]) + x
        except TypeError as e:
            rating_id = str(self.cr_data["level"]) + "_00"
        session = [1, course, course_desc, lecturer, lect_env, time, rating_id, 0]
        # print(session)
        stat = False
        try:
            if self.db.updateField(["session_start", "course_code", "desc", "lecturer_id", "lecture_env_id", "time", "rating_id", "review"],
                session, "ClassReps", self.user["id"], 'student_id')[0]:
                x, self.cr_data = self.isClassRep(self.user["id"])
                stat = True
            else:
                stat = False
        except Exception as e:
            # print(e)
            stat = False
        finally:
            if not stat:
                QMessageBox.critical(self.home, "Error", error)
            else:
                QMessageBox.information(self.home, "Success", "Session has being created successfully")
                self.home.gotoHome()
            

    def getFullDetails(self):
        try:
            i, self.lect_details = self.db.getRows("Lecturers", ['id', "title", "fname"])
            j, self.lecture_env = self.db.getRows("LectureEnv", ['id', "description"])
            k, self.courses = self.db.getRows("Courses", ['course_code', 'description'], fields = ["level"],
                                params = [self.user["level"]], withWhere = True)
            if i and j and k:
                return self.lecture_env, self.lect_details, self.courses
            return False, None, None
        except Exception as e:
            # print(e)
            return False, None, None

    def reviewSession(self, obj):
        # print(self.cr_data)
        try:
            if int(self.cr_data['session_start']) == 1:
                QMessageBox.critical(self.home, "Active Session", "Session is still active. Close Session and then you can upload data")
                obj.stackedWidget.setCurrentIndex(7)
                return
            if int(self.cr_data['review']) != 1 : 
                QMessageBox.critical(self.home, "Review Error", "No Data Available for Review and upload")
                obj.stackedWidget.setCurrentIndex(7)
                return
            field = self.grade_indices
            allGrades = list()
            x, allGrades = self.db.getRows('Gradings', field, ['rating_id'], [self.cr_data['rating_id']], withWhere = True)

            l = Auth.approx_list(Auth.sum_list(allGrades), len(allGrades))
            print(l)
            if l:
                try:
                    lect_detail = self.session_lect_details
                    lect_env = self.session_lecture_env
                except:
                    i, lect_detail = self.db.getRow("Lecturers", ["id"], [self.cr_data["lecturer_id"]])
                    j,lect_env = self.db.getRow("LectureEnv", ["id"], [self.cr_data["lecture_env_id"]])
                finally:
                    obj.reviewCourseCodeLabel.setText("<i>{0}</i>".format(self.cr_data["course_code"]))
                    obj.reviewCourseLabel.setText("<i>{0}</i>".format(self.cr_data["desc"]))
                    obj.reviewLectLabel.setText("<i>{0}. {1}</i>".format(lect_detail["title"], lect_detail["fname"]))
                    obj.reviewVenueLabel.setText("<i>{0}</i>".format(lect_env["description"]))
                    obj.reviewTimeLabel.setText("<i>{0}</i>".format(self.cr_data["time"]))
                    obj.reviewNoStudentsLabel.setText("<i>{0}</i>".format(len(allGrades)))
                    
                obj.stackedWidget.setCurrentIndex(9)
                self.aveGrade = l
                self.no_graded = len(allGrades)
            else:
                QMessageBox.warning(self.home, "Error", "No student has Graded the previous created Session. Create a new session and allow students to grade")
                return
        except Exception as e:
            raise(e)
            QMessageBox.warning(self.home, "Error", "No grading to review, Create session first for grading")
        
    def getChildren(self, childWidget):
        return self.home.findChildren(childWidget)
            
    def crUploadGrade(self, obj):
        
        QMessageBox.question(self.home, "Submit Gradings", "Are You sure you want to submit grading?")
        if QMessageBox.Yes:
            try:
                fields = self.grade_indices
                i, lect_detail = self.db.getRow("Lecturers", ['id'], [self.cr_data['lecturer_id']], col = 'db_name')
                x, self.cumGrades = self.db.getRows(lect_detail['db_name'], fields, ['course'], [self.cr_data['course_code']], withWhere = True)
                y, self.lect_grade_details_r = self.db.getRow(lect_detail['db_name'], ['course'], [self.cr_data["course_code"] + '_r'], col = 'no_lectures')
                # recent Class Grading
                fields += ['rating_id', "time", "no_graded", "lecture_env_id", "no_lectures", "validate"]
                values = self.aveGrade
                print("cum Grades",x, self.cumGrades, "Ave grade", self.aveGrade)
                self.cumGrades = list(self.cumGrades[0])
                # print(values, self.cumGrades)
                for i in range(len(self.cumGrades)):
                    self.cumGrades[i] = (self.cumGrades[i] + self.aveGrade[i])/2
                self.cumGrades = Auth.approx_list(self.cumGrades, 1)

                cont = [self.cr_data['rating_id'], self.cr_data["time"], self.no_graded, self.cr_data["lecture_env_id"],
                            self.lect_grade_details_r["no_lectures"] + 1, 1]
                values += cont 
                self.cumGrades += cont 

                a = self.db.updateField(fields, values, lect_detail['db_name'], self.cr_data["course_code"]  + '_r', "course")[0]
                b = self.db.updateField(fields, self.cumGrades, lect_detail['db_name'], self.cr_data["course_code"], "course")[0]
                if a and b:
                    self.cr_data['rating_id'] = ''
                    QMessageBox.information(self.home, "Success", "Lecture grading for {0} has being successfully uploaded".format(self.cr_data["course_code"]))
                    b = self.db.updateField(['review'], [0], 'ClassReps', self.cr_data['level'], 'level')[0]
                    self.home.gotoHome()
            except IndexError:
                QMessageBox.information(self.home, "Submit Gradings Error", "Data to be uploaded is invalid. Consider recreating session")
            except Exception as e:
                QMessageBox.information(self.home, "Submit Gradings Error", "Failed to upload, try again later")

    def crDiscardGrade(self, obj):
        try:
            QMessageBox.question(self.home, "Discard Gradings", "Are you sure you want to discard grading?")
            if QMessageBox.Yes:
                b = self.db.updateField(['review'], [0], 'ClassReps', self.cr_data['level'], 'level')[0]
                if b:
                    QMessageBox.information(self.home, "Discarded", "Gradings have being discarded")
                    self.home.gotoHome()
        except Exception as e:
            # print(e)
            QMessageBox.warning(self.home, "Error", "Could not discard grading, try again later")

    @staticmethod
    def sum_list(a_list):
        # print(a_list)
        try:
            l = [0 for i in range(len(a_list[0]))]
            for i in a_list:
                for x in range(len(i)):
                    l[x] += i[x]
            return l
        except IndexError:
            return False

    @staticmethod
    def approx_list(l, width):
        if l:
            for i in range(len(l)):
                x = l[i]/width
                if x - abs(int(x)) >= 0.5:
                    l[i] = int(x) + 1
                else:
                    l[i] = int(x)
            return l
        else:
            return False

    def reset(self):
        self.grade_indices = [i for i in ascii_lowercase][:-1]
        self.fullDetails = (None, None, None)
        self.user.clear()
        self.cr_data = {}
        print(self.user)

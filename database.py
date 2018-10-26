'''
Database implementation using sqlite3
'''
import sqlite3
from Validator import Validator


class Database(object):
    """docstring for Database"""
    tname = "Students"
    
    def __init__(self, dbname):
        '''
        Establishes secured connection to the database with given name dbname
        '''
        self.dbname = dbname        
        self.connect()
    
    def connect(self):
        print("Establishing Database Connections")
        try:
            self.conn = sqlite3.connect(self.dbname)
            self.cur = self.conn.cursor()
            
        except sqlite3.Error as e:
            raise e

    def runQuery(self, q, params=None, dict_type = False, commit=True):
        '''
        Executes a query q and binds parameter params to it
        '''
        # print(q, params)
        check = False
        self.connect()
        if sqlite3.complete_statement(q):
            data = {}
            try:
                q = q.strip()
                if params is not None:
                    self.cur.execute(q, params)
                else:
                    self.cur.execute(q)
                if q.lstrip().upper().startswith("SELECT"):
                    values = self.cur.fetchall()
                    if not dict_type:
                        key = []
                        for i in range(len(self.cur.description)):
                            key.append(self.cur.description[i][0])

                        if len(values) == 1:
                            for i, j in zip(values[0], key):
                                data[j] = i

                        if len(values) > 1:
                            x = [list() for i in range(len(values[0]))]
                            for i in values:
                                for p in range(len(i)):
                                    x[p].append(i[p])

                            for i, j in zip(key, x):
                                data[i] = j
                    else: 
                        data = values

            except sqlite3.Error as e:
                print("an Error occured: {0}".format(e.args[0]))
                raise(e)
                return False, e.args[0]
                self.conn.close()

            else:
                if commit:
                    self.save()
                return True, data
        return False, "Invalid Query"

    def save(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self, table_name, params):
        '''
        Creates a table in the database with given name table_name and columns params
        '''

        return self.runQuery("CREATE TABLE IF NOT EXISTS {0}({1});".format(table_name, params))

    def userExists(self, param, col, table_name):
        '''
        Checks if a user with username or email specified exists on the table_name

        '''
        buf = Database.stringify(col, end = ' = ?', sep = ' OR ')
        try:
            for i in param:
                if len(i) < 1:
                    return False, "Input field cannot be empty"
        except:
            pass
        x = self.runQuery("SELECT * FROM {0} WHERE {1};".format(table_name, buf), param)
        try:
            if x[0]:
                if len(x[1]) > 0:
                    return True, x[1]
                return False, "Invalid User"
        except Exception as e:
            raise(e)
            return False, e

    def addRow(self, table_name, fields, values, commit=True):
        '''
        Adds a new row into the table table_name with parameters user
        '''
        s = Database.stringify(fields, end='')
        binds = Database.stringify(fields, end='? ', inc=False)
        return self.runQuery("INSERT INTO {0}({1}) VALUES({2});".format(table_name, s, binds), values, commit)

    def getRow(self, table_name, fields, params, sep = ' AND ', col = '*'):
        '''
        Retrieves a row from a table in the database
        '''
        buf = Database.stringify(fields, end = ' = ?', sep = sep)
        return self.runQuery("SELECT {2} FROM {0} WHERE {1};".format(table_name, buf, col), params)

    def getRows(self, table_name, cur, fields = None, params = None, sep = ' AND ', withWhere = False):
        '''
        Retrieves rows from a table in the database
        '''
        if fields is not None:
            x = Database.stringify(fields, end = ' = ?', sep = sep)
            if withWhere:
                table_name += ' WHERE {0}'.format(x)

        buf = Database.stringify(cur, sep = ', ')
        
        return self.runQuery("SELECT {1} FROM {0};".format(table_name, buf), params = params, dict_type = True)

    def deleteRow(self, table_name, fields, params):
        '''
        Deletes a particular row from the table
        '''
        buf = Database.stringify(fields, end = ' = ?', sep = 'AND')
        return self.runQuery("DELETE FROM {0} WHERE {1};".format(table_name, buf), params)

    def getUser(self, u_email, password, table_name):
        '''
        retrieves a user from the database with specified email/username and password
        '''
        try:
            x, data = self.runQuery("SELECT * FROM {0} WHERE (email = ? OR username = ?) and password = ?;".format(table_name), [u_email, u_email, password])
            if not x:
                return x, data
            if len(data)<1:
                return False, "Invalid User"
            return x, data
            
        except Exception as e:
            raise e

    def updateField(self, field, value, table_name, col, i = "username"):
        '''
        updates a field in a given row with username on table table_name
        '''
        buf = Database.stringify(field, end=" = ?")
        value.append(col)
        try:
            return self.runQuery("UPDATE {0} SET {1} WHERE {2} = ?;".format(table_name, buf, i), value)
        except Exception as e:
            raise e
    
    def registerUser(self, user, commit=True):
        #check if any error
        x = Validator()
        user["username"] = user["username"].lower()
        if not x.validateUser(user)[0]:
            return x.validateUser(user)

        params = "id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(100) UNIQUE,"\
                " email VARCHAR(50) UNIQUE, password VARCHAR(255), status INTEGER NOT NULL DEFAULT 0"
        d = self.createTable(self.tname, params)
        if not d[0]:
            return d
        if self.userExists([user["username"], user["email"]], ["username", "email"], self.tname)[0]:
            return False, "User already Exists"
        return self.addRow(self.tname, list(user.keys())[:-1], list(user.values())[:-1], commit)

    def login(self, u_email, password):
        x = Validator()
        s, u_email = x.validateInput(u_email)
        if not s:
            return s, u_email
        return self.getUser(u_email, password, self.tname)

    def resetPassword(self, password, confirmP, username):
        x = Validator()
        s, x = x.validatePassword(password, confirmP)
        if not s:
            return s, x
        return self.updateField(["password"], [password], self.tname, username)

    @staticmethod
    def stringify(l, end='', sep=',', inc = True):
        buf = ""
        for x in l:
            if inc:
                buf += x
            if l[-1] != x:
                buf += end + sep
            else:
                buf += end
        return buf



        



import re


class Validator():
    """Class for Validating User inputs"""
    
    def validateUser(self, user):
        if not self.validateUsername(user['username'])[0]:
            return False, self.validateUsername(user['username'])[1]
        
        #validate email data and save to user dictionary
        if not self.validateEmail(user['email'])[0]:
            return False, self.validateEmail(user['email'])[1]
        
        #validate Password Entry
        if not self.validatePassword(user["password"], user["confirmP"])[0]:
            return False, self.validatePassword(user['password'], user['confirmP'])[1]
        
        return True, None

    def validateInput(self, input):
        #create an advance input validator
        input = input.strip()
        if len(input) < 1:
            return False, "username/email cannot be empty"
        inputRegex = re.compile(r'[!#$%&*()," {}+=/<>]')
        mo = inputRegex.search(input)
        if mo is None:
            return True, input
        return False, "username/email should not contain special characters like !@#$&*()+={[]}:;?/><"
   
    def validateUsername(self, username):
        username = username.strip()
        if len(username) < 1:
            return False, "Input Error: Username cannot be empty"
        if " " in username:
            return False, "Input Error: Username must not contain Spaces"
        
        nameRegex = re.compile(r'[!@#$%&*()"{}+=/<>]')
        mo = nameRegex.search(username)
        if mo is None:
            return True, username
        return False, "Input Error: username should not contain special characters like !@#$&*()+={[]}:;?/><"

    def validateEmail(self, email):
        email = email.strip()
        if len(email)<1:
            return False, "Input Error: Email address cannot be empty"
        emailRegex = re.compile(r'\w+@st\.futminna\.edu\.ng', re.IGNORECASE)
        mo = emailRegex.findall(email)
        if (mo is not None) and len(mo) > 0:
            return True, email
        else:
            return False, "Invalid Email Address: email must conform to the format email@st.futminna.edu.ng"

    def validatePassword(self, password, confirm_p):
        if len(password)<8:
            return False, "Input Error:Password must be more than 8 characters"
        if password != confirm_p:
            return False, "Input Error:Passwords must be the same"
        return True, password
   
    def validateDate(self, day, month, year):
        
        month_list = ["Jan", "February", "March", "April", "May","June", 
                    "July", "August", "September", "October", "November", "December"]
        leap_year = False
        Error = None
        if month == 0:
            Error = "Select a Valid Month"
        if day == 0:
            Error = "Select a Valid Day"

        if year % 4 == 0 and year % 100 != 0:
            leap_year = True
        if year % 4 != 0 and year % 100 != 0 and year % 400 == 0:
            leap_year = True

        # print(leap_year)
        if leap_year:
            if month == 2 and day > 29:
                Error = "February has only 29 days this year" 
        else:
            if month == 2 and day > 28:
                Error = "February has just 28 Days"
        if (month in [1, 3, 5, 7, 8, 10, 12]) and (day > 31):
            Error = "{0} has only 31 days".format(month_list[month])
        if (month in [4, 6, 9, 11]) and (day > 30):
                Error = "{0} has only 30 Days".format(month_list[month])
        if Error is not None:
            return False, Error
        return True, None
        
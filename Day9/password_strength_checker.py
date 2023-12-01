import re

password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"


class CheckPassword:
    def __init__(self):
        print(f'######## Password Checker Initilization ########')
        
    @classmethod
    def password_checker(self):
        password = str(input('Enter Your Password: '))
        is_strong = re.match(password_pattern, password)
        if is_strong:
            print(f'Your password {password} is strong!')
        else:
            print(f'Your password {password} is weak!')
            

password_instance = CheckPassword()
while True:
    CheckPassword.password_checker()
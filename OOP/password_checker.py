class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def check_password(self):
        password2 = input("Enter your password:")
        state = True if self.password is password2 else False
        print(f"Password is {state}")
user = User("Muhammed","09._maqa") 
user.check_password()  

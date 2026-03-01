class facebook:
    
    def __init__(self):
        self.name = "Default_user"
        self.userid = " "
        self.password = " "
        self.loggedin = False
        self.menu()

    def get_name(self):
        return self.__name

    def set_name(self, value):
        return self.__name = value

    def menu():
        user_input = input("""
            1. Please enter your email_id
            2. Please enter your password
            3. Please sign up
            4. Please sign in
        """)

        if user_input == 1:
            pass
        if user_input == 2:
            pass
        if user_input == 3:
            pass
        if user_input == 4:
            pass
    
    def enter_email():
        enter_email = input("Please enter your email ->")
        

    

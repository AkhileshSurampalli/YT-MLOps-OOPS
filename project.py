class chatbook:

    __user_id = 0

    def __init__(self):
        # to access the variable outside the method, it needs to be called with class
        self.__id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default name"
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
    
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chatbook !! How would you like to procees?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                            
                            
                            -> """)
        

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()
    
    def signup(self):
        email = input("Please enter your email -> ")
        password = input("Please enter your password here ->")
        self.username = email
        self.password = password
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password =='':
            print('please sign up first by pressing 1 in the main menu')
        else:
            uname = input("Please enter your email/uname here -> ")
            password = input("Please enter your password here: ")
            if self.username==uname and self.password==password:
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()
    
    def post(self):
        if self.loggedin == True:
            text = input("Enter your message here")
            print("Following content has been posted -> {text}")
        else:
            print("You need to sign in first to post something")
        self.menu()
    
    def send_msg(self):
        if self.loggedin== True:
            text = input("Enter your message here -> ")
            friend = input("Whom to send the message? -> ")
            print("Your message has been sent to {friend}")
        else:
            print("You need to sign in first to post something")
        print("\n")
        self.menu()

#chatbook_obj = chatbook()

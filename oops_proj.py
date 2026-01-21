class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?"
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to messege a friend
                            5. Press any other key to exit""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        print("\n")


    def signup(self):
        email = input("create your username: ")
        pwd = input("Setup your password here: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up by clicking the first option")
        else: 
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password ==pwd:
                print("You have sugned in successfully!")
                self.loggedin = True
            else:
                print("Please input correct credentials!")

        print("\n")
        self.menu()





obj = chatbook()






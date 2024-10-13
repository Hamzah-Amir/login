
# Defining Signup System Logic 
def signup():
    username = input("Enter your name: ").lower()
    password = input("Enter your password: ").lower()
    
    with open("user data.txt") as f:
        verify = f.readlines()
    for lines in verify:
        user_in_file,password_in_file = lines.strip().split(", ")   
        if user_in_file == username:
            print("Username already exist!")
            return
            
    print("Signup Successful!")
    with open("user data.txt", "a") as f:    # Writing the data in a file to save it in database
        f.write(f"{username}, {password} \n")
    
# Defining Login System Logic
def login():
    username = input("Enter your name: ").lower()
    password = input("Enter your password: ").lower()
    
    with open("user data.txt", "r") as f:   # Reading file to check if username and password is correct
        verify = f.readlines()
    
    for lines in verify:
        username_in_file,password_in_file = lines.strip().split(", ")
        
        if username_in_file == username and password_in_file == password:
            print("Login Successful")
            return
    
    print("Invalid Username or Password!")
        
# Giving user options to login or signup
while True:
    try:
        choice = input("Type, signup, login, data, exit: " ).lower()
    
        if choice == "signup":
            signup()
            
        elif choice == "login":
            login()

        elif choice == "exit":
            print("Thanks for using!")
            break

    except KeyError as e:
        print(f"You selected invalid option!")
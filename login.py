user = {}

def signup():
    username = input("Enter your name: ").lower()
    if username in user:
        print("The username already exist!")
        return

    password = input("Enter your password: ").lower()
    
    print("Signup successfull") 
    user[username] = password


def login():
    username = input("Enter your name: ").lower()
    if username not in user:
        print("User does not exist!")
        return

    password = input("Enter your password: ").lower()
    if user[username] != password:
        print("Invalid password")
    else:
        print("Login Successful")


while True:
    try:
        choice = input("Type, signup, login, data, exit:" ).lower()
    
        if choice == "signup":
            signup()
            
        elif choice == "login":
            login()
        elif choice == 'data':
            print(f"Entered date (Username,Password): {user}")

        elif choice == "exit":
            print("Thanks for using!")
            break
        else:
            print("Invalid option!")

    except Exception as e:
        print(f"An error occured {e}")

    print(user)


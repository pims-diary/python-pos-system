import Data
import AccessLevel

def login():
    """
    Prompt the user for a username and password, and check if they match
    any entry in the users dictionary.
    """
    users = Data.retrieve_users('POS(Username_password).txt')
    # Create model to store current user
    
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        is_logged_in = False

        for index in users:
            print("checking username.....")
            if users[index]['username'] == username and users[index]['password'] == password:
                name = users[index]['name']
                print("Welcome " + name + "!")
                is_logged_in = True
                break
            
        if is_logged_in:
            AccessLevel.display_options("")
        
        if not is_logged_in:
            print("Invalid username or password.")
            try_again = input("Do you want to try again? (yes/no): ").strip().lower()
            if try_again != 'yes':
                print("Exiting the login system.")
                break

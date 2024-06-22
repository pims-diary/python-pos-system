import Data
from AccessLevel import AccessLevel
from User import User
import AppDesigns


class Login:

    @staticmethod
    def perform_login():
        """
        Prompt the user for a username and password, and check if they match
        any entry in the users' dictionary.
        """
        global user
        users = Data.retrieve_users('POS(Username_password).txt')
        # Create model to store current user

        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("checking username.....")
            AppDesigns.inject_progress_bar()
            is_logged_in = False

            for index in users:
                if users[index]['username'] == username and users[index]['password'] == password:
                    name = users[index]['name']
                    AppDesigns.print_welcome_message(name)
                    is_logged_in = True
                    user = User(users[index])
                    break

            if is_logged_in:
                AccessLevel(user)

            if not is_logged_in:
                print("Invalid username or password.")
                try_again = input("Do you want to try again? (yes/no): ").strip().lower()
                if try_again != 'yes':
                    print("Exiting the login system.")
                    break

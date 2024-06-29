import Data
from AccessLevel import AccessLevel
from User import User
import AppDesigns


class Login:
    def __init__(self):
        self.user = User({})

    def perform_login(self):
        """
        Prompt the user for a username and password, and check if they match
        any entry in the users' dictionary.
        """
        users = Data.retrieve_data('POS(Username_password).txt')
        # Create model to store current user

        while True:
            username = AppDesigns.user_input("Enter your username: ")
            password = AppDesigns.user_input("Enter your password: ")
            print("checking username.....")
            # AppDesigns.inject_progress_bar()
            is_logged_in = False

            for index in users:
                if users[index]['username'] == username and users[index]['password'] == password:
                    name = users[index]['name']
                    AppDesigns.print_welcome_message(name)
                    is_logged_in = True
                    self.user = User(users[index])
                    break

            if is_logged_in:
                AccessLevel(self.user)
                return is_logged_in, self.user

            if not is_logged_in:
                print("Invalid username or password.")
                try_again = AppDesigns.user_input("Do you want to try again? (yes/no): ").strip().lower()
                if try_again != 'yes':
                    print("Exiting the login system.")
                    break

        return is_logged_in, {}

    def perform_logout(self):
        self.user = User({})

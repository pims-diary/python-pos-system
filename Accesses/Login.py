from DataSource import Data
from Accesses.AccessLevel import AccessLevel
from Accesses.DataModel.User import User
from Design import AppDesigns


class Login:
    def __init__(self):
        self.__user = User({})

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
                    self.__user = User(users[index])
                    break

            if is_logged_in:
                AccessLevel(self.__user)
                return is_logged_in, self.__user

            if not is_logged_in:
                AppDesigns.print_error('\nInvalid username or password.\n')
                try_again = AppDesigns.user_input("Do you want to try again? (yes/no): ").strip().lower()
                if try_again != 'yes':
                    print("Exiting the login system.")
                    break

        return is_logged_in, {}

    def perform_logout(self):
        self.__user = User({})

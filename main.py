from Login import Login
from AccessLevel import AccessLevel
from FeatureNavigation import FeatureNavigation
import AppDesigns


def main():
    AppDesigns.print_heading()

    while True:
        login = Login()
        login_result = login.perform_login()

        is_logged_in = login_result[0]
        user = login_result[1]

        while is_logged_in:
            access = AccessLevel(user)
            feature = access.display_access_options()
            nav = FeatureNavigation(feature, user)
            is_logged_in = nav.execute_feature()

        login.perform_logout()


    # Data.edit_customer_data('cust2@hotmail.com', Resources.CustomerField.EMAIL, 'cust41@gmail.com')


if __name__ == "__main__":
    main()

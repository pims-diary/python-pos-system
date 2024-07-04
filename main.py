from Accesses.Login import Login
from Accesses.AccessLevel import AccessLevel
from Navigation.FeatureNavigation import FeatureNavigation
from Design import AppDesigns


def main():
    AppDesigns.print_heading()

    while True:
        login = Login()
        login_result = login.perform_login()

        is_logged_in = login_result[0]
        user = login_result[1]
        AppDesigns.inject_progress_bar()

        while is_logged_in:
            access = AccessLevel(user)
            feature = access.display_access_options()
            nav = FeatureNavigation(feature, user)
            is_logged_in = nav.execute_feature()

        login.perform_logout()


if __name__ == "__main__":
    main()

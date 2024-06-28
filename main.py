from Login import Login
from AccessLevel import AccessLevel
from FeatureNavigation import FeatureNavigation
import AppDesigns


def main():
    AppDesigns.print_heading()
    login_result = Login().perform_login()

    is_logged_in = login_result[0]
    user = login_result[1]

    if is_logged_in:
        access = AccessLevel(user, {})
        feature = access.display_access_options()
        nav1 = FeatureNavigation(feature, user, {})
        result = nav1.navigate_to_feature()
        nav2 = FeatureNavigation(*result)
        nav2.navigate_to_feature()


if __name__ == "__main__":
    main()

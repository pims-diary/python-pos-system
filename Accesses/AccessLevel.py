import sys

from Design import AppDesigns
from Resources import Resources


class AccessLevel:
    feature_tuple = ()

    def __init__(self, user):
        self.user = user
        self.validate_access_by_role()

    def validate_access_by_role(self):
        if self.user.role == 'Manager':
            self.feature_tuple = (
                Resources.FEATURE_SEARCH_PRODUCT_TEXT,
                Resources.FEATURE_LIST_PRODUCTS_TEXT,
                Resources.FEATURE_SHOW_CUSTOMER_INFO_TEXT,
                Resources.FEATURE_EDIT_CUSTOMER_INFO_TEXT,
                Resources.FEATURE_CHECKOUT_TEXT,
                Resources.FEATURE_LIST_PURCHASES_TEXT,
                Resources.FEATURE_SHOW_BILL_INFO_TEXT,
                Resources.FEATURE_LOGOUT_TEXT
            )
        elif self.user.role == 'Security':
            self.feature_tuple = (
                Resources.FEATURE_SHOW_CUSTOMER_INFO_TEXT,
                Resources.FEATURE_SHOW_BILL_INFO_TEXT,
                Resources.FEATURE_LOGOUT_TEXT
            )
        elif self.user.role == 'Teller':
            self.feature_tuple = (
                Resources.FEATURE_SEARCH_PRODUCT_TEXT,
                Resources.FEATURE_LIST_PRODUCTS_TEXT,
                Resources.FEATURE_CHECKOUT_TEXT,
                Resources.FEATURE_SHOW_BILL_INFO_TEXT,
                Resources.FEATURE_LOGOUT_TEXT
            )
        else:
            print("You do not have access to the POS at the moment. Please contact the Store Manager.")
            sys.exit()

    def display_access_options(self) -> str:
        AppDesigns.print_special('Choose from the following options:')
        index = 0
        for feature in self.feature_tuple:
            index = index + 1
            print(str(index) + ': ' + feature)

        print("")
        AppDesigns.print_special("Enter the Feature Number you wish to choose.")
        print("The Feature Number is the number to the left of each feature listed above.")

        feature = self.get_feature_as_input()

        return feature

    def get_feature_as_input(self):
        while True:
            feature_number = AppDesigns.user_input("Enter here: ")

            if self.validate_feature_number(feature_number):
                feature = self.feature_tuple[int(feature_number) - 1]
                break
            else:
                print(
                    "Incorrect Feature Number. The Feature Number is the number to the left of each feature listed "
                    "above.")

        return feature

    def validate_feature_number(self, feature_number):
        if int(feature_number) <= len(self.feature_tuple):
            return True
        else:
            return False

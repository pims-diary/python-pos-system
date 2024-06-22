import sys

import AppDesigns

FEATURE_SEARCH_PRODUCT_TEXT = 'Search for a product'
FEATURE_LIST_PRODUCTS_TEXT = 'List all available products in store'
FEATURE_SHOW_CUSTOMER_INFO_TEXT = 'Display the details of the Customer'
FEATURE_CHECKOUT_TEXT = 'Checkout Items for a Customer'
FEATURE_LIST_PURCHASES_TEXT = 'List purchase history for the store'
FEATURE_SHOW_BILL_INFO_TEXT = 'Retrieve the bill details for a particular purchase'


class AccessLevel:
    feature_tuple = ()

    def __init__(self, user):
        if user.role == 'Manager':
            self.feature_tuple = (
                FEATURE_SEARCH_PRODUCT_TEXT,
                FEATURE_LIST_PRODUCTS_TEXT,
                FEATURE_SHOW_CUSTOMER_INFO_TEXT,
                FEATURE_CHECKOUT_TEXT,
                FEATURE_LIST_PURCHASES_TEXT,
                FEATURE_SHOW_BILL_INFO_TEXT
            )
        elif user.role == 'Security':
            self.feature_tuple = (
                FEATURE_SHOW_CUSTOMER_INFO_TEXT,
                FEATURE_SHOW_BILL_INFO_TEXT
            )
        elif user.role == 'Teller':
            self.feature_tuple = (
                FEATURE_SEARCH_PRODUCT_TEXT,
                FEATURE_LIST_PRODUCTS_TEXT,
                FEATURE_CHECKOUT_TEXT,
                FEATURE_SHOW_BILL_INFO_TEXT
            )
        else:
            print("You do not have access to the POS at the moment. Please contact the Store Manager.")
            sys.exit()

        feature_number = self.display_access_options()

        self.navigate_to_feature(feature_number)

    def display_access_options(self):
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

    def validate_feature_number(self, feature_number):
        if int(feature_number) <= len(self.feature_tuple):
            return True
        else:
            return False

    def get_feature_as_input(self):
        while True:
            feature_number = input("Enter here: ")

            if self.validate_feature_number(feature_number):
                feature = self.feature_tuple[int(feature_number) - 1]
                break
            else:
                print(
                    "Incorrect Feature Number. The Feature Number is the number to the left of each feature listed "
                    "above.")

        return feature

    def navigate_to_feature(self, feature):
        print("You are now on")
        print(feature + " Feature")

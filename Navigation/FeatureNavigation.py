from Resources import Resources
from Products.ManageProducts import ManageProducts
from Customers.ManageCustomers import ManageCustomers
from Accesses.AccessLevel import AccessLevel
from Checkout.Checkout import Checkout
from Transactions.ManageTransactions import ManageTransactions


def ask_to_continue():
    input('Press any key to continue to go back to the Main Menu: ')


class FeatureNavigation:
    def __init__(self, feature, user):
        self.__user = user
        self.__product = {}
        self.__feature = feature

    def execute_feature(self):
        print("")

        if self.__feature is Resources.FEATURE_SEARCH_PRODUCT_TEXT:

            search_product = ManageProducts()
            search_product.search()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_LIST_PRODUCTS_TEXT:

            list_products = ManageProducts()
            list_products.list_all_products()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_SHOW_CUSTOMER_INFO_TEXT:

            search_customer = ManageCustomers()
            search_customer.search()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_LIST_ALL_CUSTOMERS:

            search_customer = ManageCustomers()
            search_customer.list_all_customers()
            ask_to_continue()

            return True

        elif self.__feature is Resources.FEATURE_ACCESS_LEVEL_TEXT:

            AccessLevel(self.__user)
            return True

        elif self.__feature is Resources.FEATURE_CHECKOUT_TEXT:

            checkout = Checkout()
            checkout.checkout_flow()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_LIST_PURCHASES_TEXT:

            manage_bills = ManageTransactions()
            manage_bills.list_all_transactions()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_SHOW_BILL_INFO_TEXT:

            manage_bills = ManageTransactions()
            manage_bills.search()
            ask_to_continue()
            return True

        elif self.__feature is Resources.FEATURE_LOGOUT_TEXT:

            self.__user = {}
            return False

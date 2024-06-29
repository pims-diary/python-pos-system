import Resources
from ManageProducts import ManageProducts
from ManageCustomers import ManageCustomers
from AccessLevel import AccessLevel
from Checkout import Checkout


class FeatureNavigation:
    def __init__(self, feature, user):
        self.user = user
        self.product = {}
        self.feature = feature

    def execute_feature(self):
        print("")

        if self.feature is Resources.FEATURE_SEARCH_PRODUCT_TEXT:

            search_product = ManageProducts()
            search_product.search()
            return True

        elif self.feature is Resources.FEATURE_LIST_PRODUCTS_TEXT:

            list_products = ManageProducts()
            list_products.list_all_products()
            return True

        if self.feature is Resources.FEATURE_SHOW_CUSTOMER_INFO_TEXT:

            search_customer = ManageCustomers()
            search_customer.search()
            return True

        elif self.feature is Resources.FEATURE_ACCESS_LEVEL_TEXT:

            AccessLevel(self.user)
            return True

        elif self.feature is Resources.FEATURE_LOGOUT_TEXT:

            self.user = {}
            return False

        elif self.feature is Resources.FEATURE_CHECKOUT_TEXT:

            checkout = Checkout()
            checkout.checkout_for_customer()
            return True

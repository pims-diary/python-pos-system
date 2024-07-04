from enum import Enum

FEATURE_SEARCH_PRODUCT_TEXT = 'Search for a product'
FEATURE_LIST_PRODUCTS_TEXT = 'List all available products in store'
FEATURE_SHOW_CUSTOMER_INFO_TEXT = 'Display the details of the Customers'
FEATURE_EDIT_CUSTOMER_INFO_TEXT = 'Change a Customers Detail'
FEATURE_CHECKOUT_TEXT = 'Checkout Items for a Customers'
FEATURE_LIST_PURCHASES_TEXT = 'List purchase history for the store'
FEATURE_SHOW_BILL_INFO_TEXT = 'Retrieve the bill details for a particular purchase'
FEATURE_ACCESS_LEVEL_TEXT = 'Access Level'
FEATURE_LOGOUT_TEXT = 'Log out'


class CustomerField(Enum):
    EMAIL = 'Email'
    PHONE = 'Phone'
    NAME = 'Name'
    POINTS = 'Points'

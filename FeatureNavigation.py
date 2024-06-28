import Resources


class FeatureNavigation:
    def __init__(self, feature, user, product):
        self.user = user
        self.product = product
        self.feature = feature

    def navigate_to_feature(self):
        print("")

        if self.feature is Resources.FEATURE_SEARCH_PRODUCT_TEXT:

            from ManageProducts import ManageProducts
            search_product = ManageProducts(self.user, self.product)
            return search_product.search()

        elif self.feature is Resources.FEATURE_LIST_PRODUCTS_TEXT:

            from ManageProducts import ManageProducts
            list_products = ManageProducts(self.user, self.product)
            list_products.list_all_products()

        elif self.feature is Resources.FEATURE_ACCESS_LEVEL_TEXT:

            from AccessLevel import AccessLevel
            AccessLevel(self.user, self.product)

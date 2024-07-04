from Products.DataModel.Product import Product


class CartItem:
    def __init__(self):
        self.item = {}
        self.product = {}
        self.no_of_items = 0

    @property  # this is also automatically the getter
    def product(self):
        return self._product

    @product.setter
    def product(self, value: Product):
        self._product = value

    @property  # this is also automatically the getter
    def no_of_items(self):
        return self._no_of_items

    @no_of_items.setter
    def no_of_items(self, value: int):
        self._no_of_items = value

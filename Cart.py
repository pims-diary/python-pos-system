class Cart:
    def __init__(self):
        self.products = []

    @property  # this is also automatically the getter
    def products(self):
        return self.products

    @products.setter
    def products(self, value):
        self.products = value

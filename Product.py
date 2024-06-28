class Product:
    def __init__(self, product):
        self.product = product

    @property  # this is also automatically the getter
    def id(self):
        return self.product['productid']

    @id.setter
    def id(self, value):
        self.product['productid'] = value

    @property  # this is also automatically the getter
    def name(self):
        return self.product['productname']

    @name.setter
    def name(self, value):
        self.product['productname'] = value

    @property  # this is also automatically the getter
    def desc(self):
        return self.product['desc']

    @desc.setter
    def desc(self, value):
        self.product['desc'] = value

    @property  # this is also automatically the getter
    def price(self):
        return self.product['price']

    @price.setter
    def price(self, value):
        self.product['price'] = value

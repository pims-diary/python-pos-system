class Product:
    def __init__(self, product):
        self.product = product

    @property  # this is also automatically the getter
    def id(self):
        return self.product['id']

    @id.setter
    def id(self, value):
        self.product['id'] = value

    @property  # this is also automatically the getter
    def name(self):
        return self.product['name']

    @name.setter
    def name(self, value):
        self.product['name'] = value

class Transaction:
    def __init__(self):
        self.transaction = {
            'id': '',
            'email': '',
            'amount': '',
            'product': [],
            'points': ''
        }

    @property  # this is also automatically the getter
    def id(self):
        return self.transaction['id']

    @id.setter
    def id(self, value):
        self.transaction['id'] = value

    @property  # this is also automatically the getter
    def email(self):
        return self.transaction['email']

    @email.setter
    def email(self, value):
        self.transaction['email'] = value

    @property  # this is also automatically the getter
    def amount(self):
        return self.transaction['amount']

    @amount.setter
    def amount(self, value):
        self.transaction['amount'] = value

    @property  # this is also automatically the getter
    def products(self):
        return self.transaction['products']

    @products.setter
    def products(self, value):
        self.transaction['products'] = value

    @property  # this is also automatically the getter
    def points(self):
        return self.transaction['points']

    @points.setter
    def points(self, value):
        self.transaction['points'] = value

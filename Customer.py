class Customer:
    def __init__(self, customer):
        self.customer = customer

    @property  # this is also automatically the getter
    def email(self):
        return self.customer['email']

    @email.setter
    def email(self, value):
        self.customer['email'] = value

    @property  # this is also automatically the getter
    def phone(self):
        return self.customer['phone']

    @phone.setter
    def phone(self, value):
        self.customer['phone'] = value

    @property  # this is also automatically the getter
    def name(self):
        return self.customer['name']

    @name.setter
    def name(self, value):
        self.customer['name'] = value

    @property  # this is also automatically the getter
    def points(self):
        return self.customer['points']

    @points.setter
    def points(self, value):
        self.customer['points'] = value

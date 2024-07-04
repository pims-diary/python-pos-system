class TransactionItem:
    def __init__(self):
        self.transaction_item = {
            'id': '',
            'noOfItems': '',
            'price': ''
        }

    @property  # this is also automatically the getter
    def id(self):
        return self.transaction_item['id']

    @id.setter
    def id(self, value):
        self.transaction_item['id'] = value

    @property  # this is also automatically the getter
    def no_of_items(self):
        return self.transaction_item['noOfItems']

    @no_of_items.setter
    def no_of_items(self, value):
        self.transaction_item['noOfItems'] = value

    @property  # this is also automatically the getter
    def price(self):
        return self.transaction_item['price']

    @price.setter
    def price(self, value):
        self.transaction_item['price'] = value

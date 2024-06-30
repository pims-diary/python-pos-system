import Data
from Transaction import Transaction
from TransactionItem import TransactionItem


class ManageTransactions:
    data = Data.retrieve_data('POS(Transactions).txt')

    def __init__(self):
        self.a = '0'

    def search(self):
        self.a = '1'

    def save_transaction(self, email, amount, cart, points):
        transaction_data = Transaction()
        transaction_data.id = self.generate_transaction_id()
        transaction_data.email = email
        transaction_data.amount = str(amount)
        transaction_data.points = str(points)

        products = []

        for item in cart:
            transaction_item = TransactionItem()
            transaction_item.id = item.product.id
            transaction_item.no_of_items = str(item.no_of_items)
            price_of_all_items_of_product = float(item.product.price) * item.no_of_items
            transaction_item.price = str(price_of_all_items_of_product)
            products.append(transaction_item)

        transaction_data.products = products

        Data.inject_new_data('POS(Transactions).txt', transaction_data)

    def generate_transaction_id(self):
        return str(len(self.data) + 1)

    def print_transaction(self):
        self.a = '4'

    def list_all_transactions(self):
        self.a = '5'

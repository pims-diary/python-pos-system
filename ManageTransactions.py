import AppDesigns
import Data
from Transaction import Transaction
from TransactionItem import TransactionItem


def format_printable_bill(transaction_data):
    transaction_id = 'Bill No.: ' + transaction_data.id
    email = 'Customer email: ' + transaction_data.email
    amount = 'Bill Amount: ' + transaction_data.amount
    points = 'Accrued Loyalty Points' + transaction_data.points

    products = ''
    for product in transaction_data.products:
        each_product = (
                'Product ID: ' + product.id + '\n' +
                'No of Items: ' + product.no_of_items + '\n' +
                'Total price: ' + product.price + '\n' + '\n'
        )
        products = products + each_product

    printable_bill = (
            "BILL: CUSTOMER'S COPY" + '\n' +
            '---------------------' + '\n\n' +
            transaction_id + '\n' +
            email + '\n\n' +
            amount + '\n' +
            points + '\n\n' +
            'PRODUCT DETAILS' + '\n' +
            '---------------' + '\n' +
            products
    )

    return printable_bill


def ask_for_printed_copy():
    print('\nWould the customer like to have a printed copy of the Bill? ')
    response = AppDesigns.user_input('Type Y for Yes or N for No:')
    return True if response == 'Y' else False


class ManageTransactions:
    data = Data.retrieve_data('POS(Transactions).txt')
    transaction = {}

    def __init__(self):
        self.a = '0'

    def search(self):
        self.a = '1'
        AppDesigns.print_special('\nSearch Transaction / Bill:\n')
        response = AppDesigns.user_input('Please provide a Transaction ID or Bill Number: ')
        self.print_transaction(response)

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

        self.transaction = transaction_data

        Data.inject_new_data('POS(Transactions).txt', transaction_data)

    def generate_transaction_id(self):
        return str(len(self.data) + 1)

    def print_transaction(self, transaction_id='0'):
        if transaction_id == '0':
            printed_copy = format_printable_bill(self.transaction)
            Data.print_bill(printed_copy, transaction_id)
            return
        else:
            for item in self.data:
                if item.id == transaction_id:
                    printed_copy = format_printable_bill(item)
                    Data.print_bill(printed_copy, item.id)
                    return
            AppDesigns.print_error('\nThe Bill Id was not found.\n')

    def list_all_transactions(self):
        for index in range(len(self.data)):
            self.print_transaction(str(index + 1))

from Checkout.Payment.Payment import Payment

from Design import AppDesigns
from DataSource import Data


class CreditCard(Payment):
    def __init__(self):
        super().__init__()
        self.__card_validity = ''
        self.__card_number = ''

    def payment(self, bill_amount):
        response = AppDesigns.user_input('Type Y for Yes, and N for No: ')
        if response == 'Y':
            self.__card_validity = AppDesigns.user_input('\nPlease present your card: ')
            displayable_card = self.display_card(self.__card_validity)[-3:]
            secure_card = 'XXXX - XXXX - XXXX - X' + displayable_card + '\n'
            print('\nUsing the below card to complete the payment:\n')
            print(secure_card)
            if self.__card_validity == 'valid':
                AppDesigns.print_special('\nPayment Complete!\n')
                return True
            else:
                AppDesigns.print_special('\nPayment Failed! Card Transaction broke down.')
                return False

    def display_card(self, validity):
        if validity == 'valid':
            card = Data.read_credit_card('Customer_credit_card_valid.txt')
        else:
            card = Data.read_credit_card('Customer_credit_card_invalid.txt')

        self.__card_number = card['cardNumber']

        return self.__card_number

    def payment_disclosure(self):
        AppDesigns.print_special('\nDo you consent for us to scan your credit card? ')

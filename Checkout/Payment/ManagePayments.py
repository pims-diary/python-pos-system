from Design import AppDesigns


class ManagePayments:
    PAYMENT_STRING_CREDIT_CARD = 'Credit card'
    PAYMENT_STRING_CASH = 'Cash'
    PAYMENT_STRING_GO_BACK = 'Go Back to Cart'

    def __init__(self):
        self.__payment_type_action = ''
        self.__after_discount = 0.0
        self.__payment_method = ''

    def ask_for_payment_method(self):
        while True:
            print('\nWhat payment method do you wish to use for this transaction?')
            print('1. ' + self.PAYMENT_STRING_CREDIT_CARD)
            print('2. ' + self.PAYMENT_STRING_CASH)
            print('3. ' + self.PAYMENT_STRING_GO_BACK)
            response = AppDesigns.user_input('Type in one of the numbers above: ')
            if response == '1' or '2' or '3':
                if response == '1':
                    self.__payment_method = self.PAYMENT_STRING_CREDIT_CARD
                elif response == '2':
                    self.__payment_method = self.PAYMENT_STRING_CASH
                return response

    def apply_discount(self, discount_mode: str, value: float, total_amount: float):
        if discount_mode == 'percent':
            self.__after_discount = total_amount - (total_amount * (value / 100))
            return self.__after_discount
        elif discount_mode == 'exact':
            if value <= total_amount:
                self.__after_discount = total_amount - value
                return self.__after_discount
            else:
                AppDesigns.print_error('\nThe discount amount should be lesser than the Total Bill amount.\n')
                return -1.0
        else:
            print('\nSorry, something is wrong with the Discount system. The discount could not be applied.\n')
            return -1.0

    def payment_disclosure(self):
        pass

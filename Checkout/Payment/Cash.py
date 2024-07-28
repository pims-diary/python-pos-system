import math
from Checkout.Payment.Payment import Payment

from Design import AppDesigns


class Cash(Payment):
    def __init__(self):
        super().__init__()
        self.__cash_amount = 0.0
        self.__bill_amount = 0.0
        self.__balance = 0.0

    def payment(self, bill_amount):
        self.__bill_amount = bill_amount
        while True:
            print("\nPay cash now. If you want to abort cash payment press '0'")
            cash = AppDesigns.user_input('How much cash did the customer provide? $')
            if cash == '0':
                print('\nExiting Bill payment...\n')
                return False
            decimal_split = cash.split('.')
            if len(decimal_split) == 2 and len(decimal_split[1]) == 2:
                self.__cash_amount = float(cash)
                if self.__cash_amount < self.__bill_amount:
                    AppDesigns.print_error('\nThe cash provided is LESS than the bill amount.')
                    print('Customers must pay ' + str(self.__bill_amount) + ' or higher to continue')
                elif self.__cash_amount == self.__bill_amount:
                    AppDesigns.print_special('\nPayment Complete! No balance is owed to the customer.\n')
                    return True
                elif self.__cash_amount > self.__bill_amount:
                    self.__balance = self.__cash_amount - self.__bill_amount
                    if (math.ceil(self.__balance) - self.__balance) > 0.5:
                        self.__balance = math.floor(self.__balance)
                    else:
                        self.__balance = math.ceil(self.__balance)

                    if self.__balance != 0:
                        AppDesigns.print_special('\nPlease return $' + str(self.__balance) + ' to the Customers as '
                                                                                             'balance.')
                        input('Press any key after the balance is returned to Customers: ')
                    AppDesigns.print_special('\nPayment Complete! No balance is owed to the customer.\n')
                    return True
            else:
                AppDesigns.print_error('\nInvalid Amount\n')

    def payment_disclosure(self):
        AppDesigns.print_special('\nPlease inform the customer that any remaining balance in cash transaction which '
                                 'is under $0.50 will be nullified and will not be returned.\n')

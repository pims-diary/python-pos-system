import math

import AppDesigns


def execute_payment(bill_amount):
    payment_type_action = ask_for_payment_method()
    if payment_type_action == '1':
        return credit_card_payment(bill_amount)
    elif payment_type_action == '2':
        return cash_payment(bill_amount)
    elif payment_type_action == '3':
        return


def ask_for_payment_method():
    while True:
        print('\nWhat payment method do you wish to use for this transaction?')
        print('1. Credit Card')
        print('2. Cash')
        print('3. Go back to Cart')
        response = AppDesigns.user_input('Type in one of the numbers above: ')
        if response == '1' or '2' or '3':
            return response


def credit_card_payment(bill_amount):
    AppDesigns.print_special('\nDo you consent for us to scan your credit card? ')
    response = AppDesigns.user_input('Type Y for Yes, and N for No: ')
    if response == 'Y':
        card = AppDesigns.user_input('\nPlease present your card: ')
        if card == 'valid':
            # TODO: Show card details in secure mode
            #  Read from the txt file
            print('Show card details in secure mode')
            print('Continue payment')
            return True
        else:
            print('Show card details in secure mode')
            return False


def cash_payment(bill_amount):
    while True:
        print("\nPay cash now. If you want to abort cash payment press '0'")
        cash = AppDesigns.user_input('How much cash did the customer provide? $')
        if cash == '0':
            return False
        decimal_split = cash.split('.')
        if len(decimal_split) == 2 and len(decimal_split[1]) == 2:
            cash_amount = float(cash)
            if cash_amount < bill_amount:
                AppDesigns.print_error('\nThe cash provided is LESS than the bill amount.')
                print('Customer must pay ' + str(bill_amount) + ' or higher to continue')
            elif cash_amount == bill_amount:
                AppDesigns.print_special('\nPayment Complete! No balance is owed to the customer.\n')
                return True
            elif cash_amount > bill_amount:
                balance = cash_amount - bill_amount
                if (math.ceil(balance) - balance) > 0.5:
                    balance = math.floor(balance)
                else:
                    balance = math.ceil(balance)

                if balance != 0:
                    AppDesigns.print_special('\nPlease return $' + str(balance) + ' to the Customer as balance.')
                    input('Press any key after the balance is returned to Customer: ')
                AppDesigns.print_special('\nPayment Complete! No balance is owed to the customer.\n')
                return True
        else:
            AppDesigns.print_error('\nInvalid Amount\n')

from Design import AppDesigns
from Customers.ManageCustomers import ManageCustomers
from Products.ManageProducts import ManageProducts
from Checkout.DataModel.CartItem import CartItem
from Checkout.Payment.Discounts import Discounts
from . import Cart
from Checkout.Payment.ManagePayments import ManagePayments
from Checkout.Payment.CreditCard import CreditCard
from Checkout.Payment.Cash import Cash
from Checkout import LoyaltyPoints
from Transactions.ManageTransactions import ManageTransactions, ask_for_printed_copy


def no_customer_found_message():
    AppDesigns.print_special('\nNo customer was found in the database with the above mentioned email '
                             'address.\n')
    print('Do you want to add a new Customers and continue, or do you want to try a different email?')


def ask_for_purchase():
    print('\nComplete the Purchase of the above products?')
    response = AppDesigns.user_input('Type Y for Complete the Purchase and N for Continue adding items to '
                                     'Cart: ')

    if response.upper() == 'Y':
        # Place Order starts here
        return True
    else:
        # You are back in Cart
        return False


def ask_for_discount():
    print('\nDoes customer have any discounts to apply?')
    will_apply = AppDesigns.user_input('Type Y to apply discount, or type N to ignore: ')
    while True:
        if will_apply.upper() == 'Y':
            print('\nWhat mode do you want to apply the discount in:')
            print('1. Percentage')
            print('2. Exact Amount')
            print('3. Exit')
            mode_response = AppDesigns.user_input('Type 1 for PERCENTAGE, 2 for EXACT AMOUNT and 3 to EXIT: ')
            if mode_response == '1' or '2':
                response = AppDesigns.user_input('\nEnter the value of the discount: ')
                value = 0.0
                try:
                    value = float(response)
                except ValueError:
                    AppDesigns.print_error('\nInvalid Input\n')
                return mode_response, value
            else:
                return '', 0.0
        else:
            return '', 0.0


class Checkout:
    cart: list[CartItem] = []
    email = ''
    bill_amount = 0.0
    discount_applied = False
    payment = ManagePayments()
    card = CreditCard()
    cash = Cash()

    def checkout_flow(self):
        is_customer_identified = self.__identify_customer_for_checkout()
        if is_customer_identified:
            self.execute_checkout()

    def __identify_customer_for_checkout(self):
        while True:
            #   Ask for email to start checkout
            self.__collect_customer_email()
            #   Check if customer exists (ManageCustomer)
            customer_to_checkout = ManageCustomers()
            search_result = customer_to_checkout.search_customer(self.email)
            is_customer_found = customer_to_checkout.display_customer_after_search(search_result)

            if is_customer_found:
                #   If Customers exists, then continue to Add items to cart
                #   Note that the customers email is already in self.email,
                #   which means the Cart is linked to the Customers
                return True
            else:
                #   else create customer
                no_customer_found_message()
                next_step = AppDesigns.user_input('Type 1 to Add a New Customers and 2 to go back to Main Menu: ')

                if next_step == '1':
                    # Customers creation starts here
                    is_creation_complete = customer_to_checkout.create_customer()

                    if not is_creation_complete:
                        # This code may be reached if the Customers does not consent to create
                        # a database entry due to privacy. User is taken back to Main Menu.
                        return False
                    else:
                        #   Customers are created.
                        #   So link new customer to the cart
                        self.email = customer_to_checkout.customer.email
                        return True

                else:
                    return False

    def __collect_customer_email(self):
        self.email = AppDesigns.user_input("Provide the customer's email to start the checkout: ")

    def execute_checkout(self):
        # Give two options search a product or exit checkout
        AppDesigns.print_special('\nWELCOME TO THE CART\n')
        while True:
            # Add to Cart + Show Order Summary
            Cart.add_to_cart_guidelines()
            option = AppDesigns.user_input('Enter here: ')

            if option == '1':
                #   Add items to cart
                self.add_product_to_cart()
            elif option == '2':
                #   Show Order Summary
                are_items_in_cart = self.show_order_summary()
                if are_items_in_cart:
                    start_purchase = ask_for_purchase()
                    if start_purchase:
                        self.__execute_discount_flow()
                        is_payment_complete = self.__execute_payment()
                        if is_payment_complete:
                            #   Update Loyalty points for the purchase
                            points_accrued = LoyaltyPoints.points_on_purchase(self.cart)
                            LoyaltyPoints.update_loyalty_points_on_purchase(self.email, points_accrued)

                            # Create transaction for the purchase
                            manage_bill = ManageTransactions()
                            manage_bill.save_transaction(self.email, self.bill_amount, self.cart, points_accrued)

                            AppDesigns.inject_progress_bar()

                            # Show Order Summary
                            Cart.display_order_summary(self.cart)

                            # Print a copy of the bill if the customer asks for it
                            need_printed_copy = ask_for_printed_copy()
                            if need_printed_copy:
                                manage_bill.print_transaction()
                                print('\nThe receipt has been generated.')

                            AppDesigns.print_special('\nThe Purchase is Complete!')
                            return

            elif option == '3':
                exit_feature = self.__exit_checkout()
                if exit_feature:
                    break
            else:
                AppDesigns.print_error('\nInvalid input.\n')

    def add_product_to_cart(self):
        # Search for a product by ID
        # Show the product
        manage = ManageProducts()
        manage.get_product_to_search('id')

        # Ask if they want to add this product to cart
        print('\nAdd the above product to Cart?')
        response = AppDesigns.user_input('Type Y for Yes and N for No: ')

        # If yes, ask how many items of the product need to be added
        if response.upper() == 'Y':
            Cart.add_product_to_cart(self.cart, manage)
        else:
            print('\nThe product was NOT ADDED\n')

    def show_order_summary(self, discounts: Discounts = None):
        #   Show order summary and ask for placing order
        if not self.cart:
            AppDesigns.print_special('\nThere are no products in the Cart\n')
            return False
        elif len(self.cart) != 0:
            self.bill_amount = Cart.display_order_summary(self.cart, discounts)
            return True

    def __exit_checkout(self):
        print('\nAre you sure you want to exit the Checkout?')
        AppDesigns.print_special('Note that you will lose all products in Cart if you exit Checkout')
        response = AppDesigns.user_input('Type Y for Yes and N for No: ')

        if response.upper() == 'Y':
            self.cart.clear()
            self.email = ''
            self.bill_amount = 0.0
            self.discount_applied = False
            return True
        else:
            return False

    def __execute_discount_flow(self):
        if not self.discount_applied:
            discounts = Discounts()
            discount_info = ask_for_discount()
            discounts.mode = discount_info[0]
            discounts.value = discount_info[1]
            if discounts.mode == '1':
                discounts.discounted_amount = self.payment.apply_discount('percent', discounts.value, self.bill_amount)
                self.bill_amount = discounts.discounted_amount
                self.show_order_summary(discounts)
                self.discount_applied = True
            elif discounts.mode == '2':
                discounts.discounted_amount = self.payment.apply_discount('exact', discounts.value, self.bill_amount)
                self.bill_amount = discounts.discounted_amount
                self.show_order_summary(discounts)
                self.discount_applied = True

    def __execute_payment(self):
        payment_type_action = self.payment.ask_for_payment_method()
        if payment_type_action == '1':
            self.card.payment_disclosure()
            return self.card.payment(self.bill_amount)
        elif payment_type_action == '2':
            self.cash.payment_disclosure()
            return self.cash.payment(self.bill_amount)
        elif payment_type_action == '3':
            print('\nExiting Bill Payment...\n')
            return

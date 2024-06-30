import AppDesigns
from ManageCustomers import ManageCustomers
from ManageProducts import ManageProducts
from CartItem import CartItem
import Cart
import Payment
import LoyaltyPoints
from ManageTransactions import ManageTransactions


def exit_checkout():
    print('\nAre you sure you want to exit the Checkout?')
    AppDesigns.print_special('Note that you will lose all products in Cart if you exit Checkout')
    response = AppDesigns.user_input('Type Y for Yes and N for No: ')

    if response.upper() == 'Y':
        return True
    else:
        return False


def no_customer_found_message():
    AppDesigns.print_special('\nNo customer was found in the database with the above mentioned email '
                             'address.\n')
    print('Do you want to add a new Customer and continue, or do you want to try a different email?')


def ask_for_purchase():
    print('\nComplete the Purchase of the above products?')
    response = AppDesigns.user_input('Type Y for Complete the Purchase and N for Continue adding items to '
                                     'Cart: ')

    if response.upper() == 'Y':
        print('\nPlace Order starts here.\n')
        return True
    else:
        print('\nYou are back in the Cart.\n')
        return False


class Checkout:
    cart: list[CartItem] = []
    email = ''
    bill_amount = 0.0

    def checkout_flow(self):
        is_customer_identified = self.identify_customer_for_checkout()
        if is_customer_identified:
            self.execute_checkout()

    def identify_customer_for_checkout(self):
        while True:
            #   Ask for email to start checkout
            self.collect_customer_email()
            #   Check if customer exists (ManageCustomer)
            customer_to_checkout = ManageCustomers()
            search_result = customer_to_checkout.search_customer(self.email)
            is_customer_found = customer_to_checkout.display_customer_after_search(search_result)

            if is_customer_found:
                #   If Customer exists, then continue to Add items to cart
                #   Note that the customers email is already in self.email,
                #   which means the Cart is linked to the Customer
                return True
            else:
                #   else create customer
                no_customer_found_message()
                next_step = AppDesigns.user_input('Type 1 to Add a New Customer and 2 to Try a different email: ')

                if next_step == '1':
                    # Customer creation starts here
                    is_creation_complete = customer_to_checkout.create_customer()

                    if not is_creation_complete:
                        # This code may be reached if the Customer does not consent to create
                        # a database entry due to privacy. User is taken back to Main Menu.
                        return False
                    else:
                        #   Customer is created.
                        #   So link new customer to the cart
                        self.email = customer_to_checkout.customer.email
                        return True

                else:
                    return False

    def collect_customer_email(self):
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
                        is_payment_complete = Payment.execute_payment(self.bill_amount)
                        if is_payment_complete:
                            #   Update Loyalty points for the purchase
                            points_accrued = LoyaltyPoints.points_on_purchase(self.cart)
                            LoyaltyPoints.update_loyalty_points_on_purchase(self.email, points_accrued)

                            # Create transaction for the purchase
                            manage_bill = ManageTransactions()
                            manage_bill.save_transaction(self.email, self.bill_amount, self.cart, points_accrued)

                            # Show Order Summary
                            Cart.display_order_summary(self.cart)

                            #   TODO:
                            #    Print transaction as a separate txt file (ManageTransaction)

                            return

            elif option == '3':
                exit_feature = exit_checkout()
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

    def show_order_summary(self):
        #   Show order summary and ask for placing order
        if not self.cart:
            AppDesigns.print_special('\nThere are no products in the Cart')
            return False
        elif len(self.cart) != 0:
            self.bill_amount = Cart.display_order_summary(self.cart)
            return True

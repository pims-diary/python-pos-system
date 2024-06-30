import AppDesigns
from ManageCustomers import ManageCustomers
from ManageProducts import ManageProducts
from CartItem import CartItem
import Cart


def add_to_cart_guidelines():
    print('Choose from the following options:')
    print('1. Add a product to Cart')
    print('2. Show Order Summary')
    print('3. Exit Checkout')
    print('Type in 1, 2 or 3 to choose one of the above options')


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


class Checkout:
    cart: list[CartItem] = []
    email = ''

    def checkout_for_customer(self):
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
                self.add_to_cart()
                return
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
                        return
                    else:
                        #   Customer is created.
                        #   So link new customer to the cart
                        self.email = customer_to_checkout.customer.email
                        #   Add items to cart
                        self.add_to_cart()
                        return

                else:
                    return

    #   TODO:Place order and show transaction summary
    #   TODO: Increase customer loyalty points
    #   TODO: Store transaction details (ManageTransaction)
    #   TODO: Print transaction as a separate txt file (ManageTransaction)

    def collect_customer_email(self):
        self.email = AppDesigns.user_input("Provide the customer's email to start the checkout: ")

    def add_to_cart(self):
        # Give two options search a product or exit checkout
        AppDesigns.print_special('\nWELCOME TO THE CART\n')
        while True:
            add_to_cart_guidelines()
            option = AppDesigns.user_input('Enter here: ')

            if option == '1':
                self.add_product_to_cart()
            elif option == '2':
                self.show_order_summary()
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
        elif len(self.cart) != 0:
            Cart.display_order_summary(self.cart)
            print('\nComplete the Purchase of the above products?')
            response = AppDesigns.user_input('Type Y for Complete the Purchase and N for Continue adding items to '
                                             'Cart: ')

            if response.upper() == 'Y':
                print('\nPlace Order starts here.\n')
            else:
                print('\nYou are back in the Cart.\n')

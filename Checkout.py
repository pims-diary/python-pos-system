import AppDesigns
from ManageCustomers import ManageCustomers
from ManageProducts import ManageProducts
from CartItem import CartItem


def add_to_cart_guidelines():
    print('Choose from the following options:')
    print('1. Add a product to Cart')
    print('2. Proceed to Order Summary')
    print('3. Exit Checkout')
    print('Type in 1, 2 or 3 to choose one of the above options')


class Checkout:
    cart: list[CartItem] = []
    email = ''

    def checkout_for_customer(self):
        #   Ask for email to start checkout
        self.collect_customer_email()
        #   Check if customer exists (ManageCustomer)
        customer_to_checkout = ManageCustomers()
        search_result = customer_to_checkout.search_customer(self.email)
        #   If yes, link to the customer to the cart
        is_search_complete = customer_to_checkout.display_customer_after_search(search_result)

        if is_search_complete:
            #   Add items to cart
            self.add_to_cart()
        #   else create customer (ManageCustomer)
        else:
            # TODO: Add some information that says the customer was not found
            #  and Do you want to create a new customer?
            # TODO: If not, then send them back to Access page
            is_creation_complete = customer_to_checkout.create_customer()

            if not is_creation_complete:
                return
            else:
                #   Link new customer to the cart
                self.email = customer_to_checkout.customer.email
                #   Add items to cart
                self.add_to_cart()

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
                break
            elif option == '3':
                # Do something
                break
            else:
                AppDesigns.print_error('\nInvalid input.\n')

        # TODO: If no, back to search options
        # TODO: if exit is selected, then notify that items in Cart will not stay saved.

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
            print('\nHow many items of this product do you want to add?')
            while True:
                item_response = AppDesigns.user_input('Type in a number: ')
                try:
                    item_count = int(item_response)
                    break
                except ValueError:
                    AppDesigns.print_error('\nInvalid Input\n')

            new_item = CartItem()
            is_item_in_cart = False
            for index, item in enumerate(self.cart):
                if item.product.id == manage.product.id:
                    is_item_in_cart = True
                    # Add to cart and go back to search options
                    new_item.no_of_items = item.no_of_items + item_count
                    new_item.product = manage.product
                    self.cart[index] = new_item
                    break
            if not is_item_in_cart:
                # Add to cart and go back to search options
                new_item.no_of_items = item_count
                new_item.product = manage.product
                self.cart.append(new_item)
            AppDesigns.print_special('\nPRODUCT ADDED!\n')
        else:
            print('\nThe product was NOT ADDED\n')

    def show_order_summary(self):
        #   Show order summary and ask for placing order
        if not self.cart:
            AppDesigns.print_special('\nThere are no products in the Cart')
        elif len(self.cart) != 0:
            AppDesigns.print_special('\nORDER SUMMARY:\n')
            for index, item in enumerate(self.cart):
                # TODO: Stylise with table
                print('Item #' + str(index + 1))
                print(item.product.name)
                print(item.no_of_items)
                print('')

from DataSource import Data
from Design import AppDesigns
from Customers.DataModel.Customer import Customer


class ManageCustomers:
    customers = Data.retrieve_data('POS(Customer_details).txt')

    def __init__(self):
        self.customer = Customer(
            {
                'email': '',
                'phone': '',
                'name': '',
                'points': ''
            }
        )

    def search(self):
        AppDesigns.print_special("SEARCH A CUSTOMER...")
        is_search_complete = False
        while not is_search_complete:
            print("\nPlease provide the email address of the customer.")
            email = AppDesigns.user_input("Enter here: ")
            print("")
            is_search_complete = self.search_and_display_customer(email)

        print("\nExiting Customers Search...\n")

    def search_and_display_customer(self, email):
        search_result = self.search_customer(email)

        is_search_complete = self.display_customer_after_search(search_result)

        return is_search_complete

    def search_customer(self, email):
        for index in self.customers:
            if self.customers[index]['email'] == email:
                self.customer = Customer(self.customers[int(index)])
                return True
        return False

    def display_customer_after_search(self, search_result):
        if search_result is False:
            AppDesigns.print_error("\nThis customer was not found.\n")
            return False
        elif search_result and len(self.customer.customer) != 0:
            AppDesigns.print_special("\nCUSTOMER DETAILS")
            print("Email ID: " + self.customer.email)
            print("Phone Number: " + self.customer.phone)
            print("Customers Name: " + self.customer.name)
            print("Loyalty points: " + self.customer.points)
            return True
        else:
            AppDesigns.print_error("\nOops. Something wrong with this request. Please try again.\n")
            return False

    def list_all_customers(self):
        AppDesigns.print_special("\nLIST OF ALL CUSTOMERS AVAILABLE")
        for index in self.customers:
            print("")
            self.customer = Customer(self.customers[int(index)])
            print("Email ID: " + self.customer.email)
            AppDesigns.print_special("Customers Name: " + self.customer.name)
            self.customer = {}
        print("\nExiting Customers List...\n")

    def create_customer(self):
        AppDesigns.print_special('\n\nCreate a New Customers')
        print('\nNOTE: Before registering the Customers, please inform them that their email address and phone number '
              'will be stored in our system and ask if they consent for it.')
        consent = AppDesigns.user_input('Do they consent on having their email and phone number stored? Type Y for '
                                        'Yes and N for No: ')
        if consent != 'Y':
            return False
        else:
            email = AppDesigns.user_input('\nType in the email address of the customer: ')
            phone = AppDesigns.user_input('\nType in the phone number of the customer: ')
            name = AppDesigns.user_input('\nType in the name of the customer: ')

            self.customer.email = email
            self.customer.phone = phone
            self.customer.name = name
            self.customer.points = '0'

            Data.inject_new_data("POS(Customer_details).txt", self.customer)
            AppDesigns.print_special('\nSuccess! The new customer is created.')
            AppDesigns.print_special("\nCUSTOMER DETAILS")
            print("Email ID: " + self.customer.email)
            print("Phone Number: " + self.customer.phone)
            print("Customers Name: " + self.customer.name)
            print("Loyalty points: " + self.customer.points)
            print("\nExiting Customers Creation...\n")
            return True

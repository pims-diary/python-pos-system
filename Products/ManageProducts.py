from DataSource import Data
from Design import AppDesigns
from Products.DataModel.Product import Product


def search_guidelines():
    print("You can search based on:")
    print("1. Product ID")
    print("2. Product Name\n")
    print("Enter 1 to search by ID, enter 2 to search by Name, enter 0 to exit")


class ManageProducts:
    products = Data.retrieve_data('POS(Product_details).txt')

    def __init__(self):
        self.product = Product(
            {
                'id': '',
                'name': '',
                'desc': '',
                'price': '',
                'points': ''
            }
        )

    def search(self):
        AppDesigns.print_special("SEARCH A PRODUCT...\n")
        self.get_search_type()

    def get_search_type(self):
        while True:
            search_guidelines()
            search_criteria = AppDesigns.user_input("Enter here: ")

            if search_criteria == '1':
                print("")
                self.get_product_to_search('id')
                break
            elif search_criteria == '2':
                print("")
                self.get_product_to_search('name')
                break
            elif search_criteria == '0':
                break
            else:
                AppDesigns.print_error("\nInvalid Input\n")

            print("\nExiting Product Search...\n")

    def get_product_to_search(self, by):
        search_criteria = 'ID' if by == 'id' else 'Name'
        while True:
            AppDesigns.print_special("\nEnter a Product " + search_criteria + ".")
            value = AppDesigns.user_input("Enter here: ")

            is_search_successful = self.search_product(by, value)

            if not is_search_successful:
                AppDesigns.print_error("\nThis product was not found.\n")
            elif is_search_successful and len(self.product.product) != 0:
                AppDesigns.print_special("\nPRODUCT DETAILS")
                print("Product ID: " + self.product.id)
                print("Product Name: " + self.product.name)
                print("Description: " + self.product.desc)
                print("Unit price: " + self.product.price)
                print("Loyalty points: " + self.product.points)
                break
            else:
                AppDesigns.print_error("\nOops. Something wrong with this request. Please try again.\n")

    def search_product(self, by, value):
        search_criteria = 'productid' if by == 'id' else 'productname'

        for index in self.products:
            if self.products[index][search_criteria] == value:
                self.product = Product(self.products[int(index)])
                return True
        return False

    def list_all_products(self):
        AppDesigns.print_special("\nLIST OF ALL PRODUCTS AVAILABLE IN STORE")
        for index in self.products:
            print("")
            self.product = Product(self.products[int(index)])
            print("Product ID: " + self.product.id)
            AppDesigns.print_special("Product Name: " + self.product.name)
            self.product = {}
        print("\nExiting Product List...\n")

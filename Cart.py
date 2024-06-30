from rich.console import Console
from rich.table import Table

import AppDesigns

from CartItem import CartItem
from ManageProducts import ManageProducts


def display_order_summary(cart):
    print('')
    table = Table(title="ORDER SUMMARY")
    table.add_column("Item #", justify="right")
    table.add_column("Product Name", style="magenta")
    table.add_column("No of Items", style="dodger_blue2")
    table.add_column("Total Price", justify="right", style="green")

    amount = 0.0
    for index, item in enumerate(cart):
        amount = amount + (float(item.product.price) * item.no_of_items)
        table.add_row(
            str(index + 1),
            item.product.name,
            str(item.no_of_items),
            '$' + str(float(item.product.price) * item.no_of_items)
        )

    console = Console()
    console.print(table)
    AppDesigns.print_special('\nTOTAL BILL: ' + '$' + str(amount) + '\n')
    return amount


def add_product_to_cart(cart: list[CartItem], manage: ManageProducts):
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
    for index, item in enumerate(cart):
        if item.product.id == manage.product.id:
            is_item_in_cart = True
            # Add to cart and go back to search options
            new_item.no_of_items = item.no_of_items + item_count
            new_item.product = manage.product
            cart[index] = new_item
            break
    if not is_item_in_cart:
        # Add to cart and go back to search options
        new_item.no_of_items = item_count
        new_item.product = manage.product
        cart.append(new_item)
    AppDesigns.print_special('\nPRODUCT ADDED!\n')


def add_to_cart_guidelines():
    print('Choose from the following options:')
    print('1. Add a product to Cart')
    print('2. Show Order Summary')
    print('3. Exit Checkout')
    print('Type in 1, 2 or 3 to choose one of the above options')

from DataSource import Data
from Resources import Resources
from Customers.ManageCustomers import ManageCustomers


def points_on_purchase(cart):
    points = 0
    for index, item in enumerate(cart):
        points = points + (int(item.product.points) * item.no_of_items)
    return points


def update_loyalty_points_on_purchase(customer_email, points_accrued):
    manage = ManageCustomers()
    manage.search_customer(customer_email)
    # current_points = int(manage.customer.points)
    # updated_points = current_points + points_accrued
    # Data.edit_customer_data(customer_email, Resources.CustomerField.POINTS, str(updated_points))

import traceback

import AppDesigns
import Resources


def retrieve_data(file_path):
    """
    retrieve data from a file and return a dictionary.
    """
    data = {}
    index = 1
    try:
        with open(file_path, 'r') as file:
            for line in file:
                file_line = line.split(',')
                if file_path == 'POS(Username_password).txt':
                    data_unit = retrieve_user_data(file_line)
                elif file_path == 'POS(Product_details).txt':
                    data_unit = retrieve_product_data(file_line)
                elif file_path == 'POS(Customer_details).txt':
                    data_unit = retrieve_customer_data(file_line)
                elif file_path == 'POS(Transactions).txt':
                    data_unit = retrieve_transaction_data(file_line)
                data[index] = data_unit
                index = index + 1
    except FileNotFoundError:
        raise Exception("There seems to be some issue with the data. Please contact Store Manager immediately.")
    except UnboundLocalError:
        print(traceback.format_exc())
        raise Exception("There seems to be some issue with the data. Please contact Store Manager immediately.")
    return data


def retrieve_user_data(file_line):
    user = {
        'username': file_line[0],
        'password': file_line[1],
        'name': file_line[2],
        'role': file_line[3]
    }
    return user


def retrieve_product_data(file_line):
    product = {
        'productid': file_line[0],
        'productname': file_line[1],
        'desc': file_line[2],
        'price': file_line[3],
        'points': file_line[4]
    }
    return product


def retrieve_customer_data(file_line):
    product = {
        'email': file_line[0],
        'phone': file_line[1],
        'name': file_line[2],
        'points': file_line[3]
    }
    return product


def retrieve_transaction_data(file_line):
    products_list = file_line[3].split(':')
    products = []
    for product in products_list:
        properties = product.split(' ')
        each_product = {
            'id': properties[0],
            'noOfItems': properties[1],
            'price': properties[2]
        }
        products.append(each_product)

    transaction = {
        'id': file_line[0],
        'email': file_line[1],
        'amount': file_line[2],
        'products': products,
        'points': file_line[4]
    }
    return transaction


def inject_new_data(file_path, data):
    """
    write data to a file
    """
    try:
        file = open(file_path, 'a')
        line = ''
        if file_path == 'POS(Username_password).txt':
            line = write_user_data(data)
        elif file_path == 'POS(Product_details).txt':
            line = write_product_data(data)
        elif file_path == 'POS(Customer_details).txt':
            line = write_customer_data(data)
        elif file_path == 'POS(Transactions).txt':
            line = write_transaction_data(data)
        if line != '':
            file.write('\n' + line)
    except FileNotFoundError:
        raise Exception("There seems to be some issue with the data. Please contact Store Manager immediately.")


def write_user_data(user):
    return user.username + ',' + user.password + user.name + user.role


def write_product_data(product):
    return product.id + ',' + product.name + ',' + product.desc + ',' + product.price + ',' + product.points


def write_customer_data(customer):
    return customer.email + ',' + customer.phone + ',' + customer.name + ',' + customer.points


def write_transaction_data(transaction):
    products_list = ''
    for product in transaction.products:
        product_string = product.id + ' ' + str(product.no_of_items) + ' ' + str(product.price)
        if products_list != '':
            products_list = products_list + ';' + product_string
        else:
            products_list = product_string
    return (
            transaction.id
            + ',' + transaction.email
            + ',' + transaction.amount
            + ',' + products_list
            + ',' + transaction.points
    )


def edit_customer_data(email, field_name, value):
    """
    Edit one of the fields for a Customer
    """
    line_to_edit = ''
    with open('POS(Customer_details).txt', 'r') as file:
        for line in file:
            if email in line:
                line_to_edit = line
                break

    if line_to_edit != '':
        file_line = line_to_edit.split(',')
    else:
        AppDesigns.print_error('This customer info was not found. Please check if the input details are correct.')
        return

    new_line = ''

    if field_name == Resources.CustomerField.EMAIL:
        new_line = value + ',' + file_line[1] + ',' + file_line[2] + ',' + file_line[3]
    elif field_name == Resources.CustomerField.PHONE:
        new_line = file_line[0] + ',' + value + ',' + file_line[2] + ',' + file_line[3]
    elif field_name == Resources.CustomerField.NAME:
        new_line = file_line[0] + ',' + file_line[1] + ',' + value + ',' + file_line[3]
    elif field_name == Resources.CustomerField.POINTS:
        new_line = file_line[0] + ',' + file_line[1] + ',' + file_line[2] + ',' + value + '\n'

    if new_line != '':
        with open("POS(Customer_details).txt", 'r') as customer_file:
            contents = customer_file.read()

        with open("POS(Customer_details).txt", 'w') as file:
            file.write(contents.replace(line_to_edit, new_line))
    else:
        AppDesigns.print_error('This field name for customer is not configured in the program. Please report this to '
                               'the Manager. Field Name: ' + field_name)

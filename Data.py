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
                data[index] = data_unit
                index = index + 1
    except FileNotFoundError:
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
        'price': file_line[3]
    }
    return product


def inject_data(file_path, data):
    """
    write data to a file
    """
    try:
        file = open(file_path, 'w')
        line = ''
        if file_path == 'POS(Username_password).txt':
            line = write_user_data(data)
        elif file_path == 'POS(Product_details).txt':
            line = write_product_data(data)
        elif file_path == 'POS(Product_details).txt':
            line = write_customer_data(data)
        if line != '':
            file.write('\n' + line)
    except FileNotFoundError:
        raise Exception("There seems to be some issue with the data. Please contact Store Manager immediately.")


def write_user_data(user):
    return user['username'] + ',' + user['password'] + user['name'] + user['role']


def write_product_data(product):
    return product['productid'] + ',' + product['productname'] + product['desc'] + product['price']


def write_customer_data(customer):
    return customer['email'] + ',' + customer['name'] + customer['phone'] + customer['rewardpoints']

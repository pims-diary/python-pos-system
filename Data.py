def retrieve_users(file_path):
    """
    retrieve users from a file and return a dictionary with usernames as keys
    and passwords as values.
    """
    data = {}
    index = 1
    with open(file_path, 'r') as file:
        for line in file:
            file_line = line.split(',')
            if file_path == 'POS(Username_password).txt':
                data_unit = retrieve_user_data(file_line)
            elif file_path == 'POS(Product_details).txt':
                data_unit = retrieve_product_data(file_line)
            data[index] = data_unit
            index = index + 1
    return data


def retrieve_user_data(file_line):
    user = {}
    user['username'] = file_line[0]
    user['password'] = file_line[1]
    user['name'] = file_line[2]
    user['role'] = file_line[3]
    return user


def retrieve_product_data(file_line):
    product = {}
    product['productid'] = file_line[0]
    product['productname'] = file_line[1]
    return product
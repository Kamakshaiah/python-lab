import string

customers = list(string.ascii_uppercase)
passwords = list(range(len(customers)))

def make_data(customers=customers, passwords=passwords):
    return dict(zip(customers, passwords))

data = make_data()

def print_data(customer=None, customers=customers, passwords=passwords):
    if customer == None:
        print([(i, j) for i,j in zip(data['customers'], data['passwords'])])
    else:
        print([(i, j) for i,j in zip(data['customers'], data['passwords']) if i == customer])

def find_password(customer=None):
    if customer == None:
        print([(i, j) for i,j in zip(data['customers'], data['passwords'])])
    else:
        customer = [(i, j) for i,j in zip(data['customers'], data['passwords']) if i == customer]
        return customer[0][1]

def change_password(customer=None):
    # print(type(customer))
    global data
    a_u = input('input your token ')
    if a_u == 'xyz':
        new_pass = input('Input password ')
        # print('the password type %s' %type(new_pass))
        
        # d = next(i for i in data if i[customer] == customer)
        # print('the d type %s' %type(d))
        # print('the type of d customer {type(d[customer])}')
        data[customer] = int(new_pass)
        return data


    
        
if __name__ == '__main__':
    data = make_data()
    print(data)
##    print_data(customer='A')
##    print(find_password(customer='A'))
    print(change_password(customer='A'))

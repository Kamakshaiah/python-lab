# CRUD

import string

#create 
customers = list(string.ascii_uppercase)

#retrieve
def show_customers():
    print(customers)

#update
def add_customer(customer):
    global customers
    customers.append(customer)
    return customers
    
#delete
def delete_customer(customer, customers = customers):
    return [i for i in customers if i != customer]
    
def change_name(customer=None,new_customer=None):
    global customers
    if customer in customers:
        customers[customers.index(customer)] = new_customer
    return customers
    
if __name__ == '__main__':

    # print(show_customers())
    # customers = delete_customer('B')
    # customers = add_customer('A')
    # print(customers)
    print(change_name(customer='B', new_customer='A'))
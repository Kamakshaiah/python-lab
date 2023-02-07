# creating and appending tuples [using lists]

import string

names = tuple()
print(names)
name_list = list(names)

print(name_list)

name_list = [i for i in string.ascii_uppercase[0:5]]

names_1 = tuple(name_list)
names = names_1
del(names_1)

print(f'names {names}')

# example

users = list(string.ascii_uppercase[0:5])
users_tuple = tuple(users)
print(f'users {users_tuple}')

# numbers

import random

passwords = random.sample(range(10000, 99999), 10)
print(passwords)

# dictionary

# user_data = dict(zip(users, passwords))
# print(user_data)
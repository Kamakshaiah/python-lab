import operator
operator.__lt__(1, 2)
operator.__lt__(2, 1)
operator.__add__(1, 2)
operator.__pow__(2, 3)

data = [i for i in range(10)]

# map using lambda function

list(map(lambda i: i **2, data))

# map using UDF

def mapoper(x):
    if x > 3 and x < 8:
        return x**2
list(map(mapoper, data))

# map using operator module for two inputs (args)

from operator import pow
from itertools import repeat
list(map(pow, [1,2,3], repeat(4)))

list(map(pow, [1,2,3], repeat(2)))

# filter with lambda function

list(filter(lambda i: i >3, range(10)))
list(filter(lambda i: i >3 and i < 8, range(10)))

# filter with user defined function (UDF)

def filteroper(x):
    if x > 3:
        return x

list(filter(filteroper, range(10)))

def filteroper(x):
    if x > 3 and x < 8:
        return x

list(filter(filteroper, range(10)))

# filter together with map functions

list(map(lambda x: x **2, list(filter(lambda i: i >3 and i < 8, range(10)))))

# reduce function

reduce(lambda x, y: x * y, range(1, 10))
reduce(lambda x, y: x ** y, range(1, 10)) # 1
reduce(lambda x, y: x ** y, range(2, 4)) # 8
reduce(lambda x, y: x ** y, range(2, 5)) # 4096

def addition(x, y):
    return x + y

reduce(addition, range(2, 10)) # 44

def product(x, y):
    return x * y

reduce(product, range(2, 10)) # 362880

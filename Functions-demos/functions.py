# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:47:22 2023

@author: GIM
"""

def Range(n):
    cnt = 0
    while cnt < n:
        print(cnt)
        cnt += 1
    
def data_type(x):
    if type(x) == int:
        print(f'{x} is of interger type')
    else:
        print(f'{x} is not interger type')
        
# data_type(1)
# Range(5)

fadd = lambda x, y: x + y
fmul = lambda x, y: x*y
fadd(1, 2)
# fmul([1, 2, 3, 4, 5]) # will not work

import functools 
functools.reduce(lambda x, y: x * y, range(1, 5))
res = map(fmul, range(1, 5), range(1, 5))
# list(res)
# set(res)
list(map(fmul, range(1, 5), range(1, 5)))
set(map(fmul, range(1, 5), range(1, 5)))

list(filter(lambda x: x <0, range(-5, 5)))

list(filter(lambda x: x > 0, range(-5, 5)))

# arithmetic mean

def Mean(x):
    return sum(x)/len(x)

Mean(range(5))

def meanMaxMin(vec, *args):
    ''' This function creates Maximum and
        Minimum along with Mean as by user
        arguments.
        Arguments:
            vec: Input vector
            *args: positional arguments. eg. 'min'
                and 'max'
            Output: Returns default value: mean and either
        minumum or maximum by argument.
    '''
    
    out1 = Mean(vec)
    
    if 'max' in args:
        out2 = max(vec)
        return({'mean ': out1, 'max':out2})
    if 'min' in args:
        out2 = min(vec)
        return({'mean ': out1, 'min':out2})
    
meanMaxMin(range(1, 11), 'min')
meanMaxMin(range(1, 11), 'max')

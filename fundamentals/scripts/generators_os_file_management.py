# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:58:13 2023

@author: DrMk
@title: Generators
"""

# the purpose of generator is to handle big data 

t = (i for i in range(5))
# len(t) # does not work
for i in t:
    print(i)
    
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

for i in range(5):
    next(gen)
    
# for i in range(5):
    # yield gen # not correct

## using generators for file management    

import os
os.getcwd()
os.chdir('D:\\Miscel')
os.getcwd()
open('file.txt', 'a').close() # creates an empty file

def random_num_writer():
    with open('file.txt', 'a') as file:
        file.write(str(next(gen)))
        file.write('\n')
        
for i in range(100):
    random_num_writer()


# less efficient 

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

# more efficient
# open('file.txt', 'a').close()

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
    
filegen = csv_reader('file.txt')

for i in range(5):
    print(next(filegen))

## application - palindrome

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
    
for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(i)
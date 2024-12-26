# syntax error

##amount = 10000
##if(amount > 2999)
##print("You are eligible to purchase Dsa Self Paced")

# division by zero 

marks = 1000
##a = marks / 0
##print(a)

##if marks < 10000:
##    try:
##        marks/0
##    except ZeroDivisionError:
##        print('zero division error')
    
# type error

##x = 5
##y = "hello"
##z = x + y

# except type error

##x = 5
##y = "hello"
##try:
##    z = x + y
##except TypeError:
##    print("Error: cannot add an int and a str")

# index error

##a = [1, 2, 3]
##
##try: 
##    print ("Second element = %d" %(a[1]))
##
##    print ("Fourth element = %d" %(a[3]))
##
##except:
##    print ("An error occurred")

# name error [arguments]

##def fun(a):
##    if a < 4:
##
##        b = a/(a-3)
##    print("Value of b = ", b)
##    
##try:
##    fun(5)
##    
##except ZeroDivisionError:
##    print("ZeroDivisionError Occurred and Handled")
##except NameError:
##    print("NameError Occurred and Handled")

# try with else
##
##def AbyB(a , b):
##    try:
##        c = ((a+b) / (a-b))
##    except ZeroDivisionError:
##        print ("a/b result in 0")
##    else:
##        print (c)
##AbyB(2.0, 3.0)
##AbyB(3.0, 3.0)

##try:
##    k = 5//0 
##    print(k)
##
##except ZeroDivisionError:
##    print("Can't divide by zero")
##
##finally:
##    print('This is always executed')

# raising errors

try: 
    raise NameError("Hi there")
except:
    print ("An exception")
    raise

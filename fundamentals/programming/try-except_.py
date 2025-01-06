###1. basic try-except
##
##x = 12.5
##try:
##  print(x)
##except NameError:
##  print("Variable x is not defined")
##except:
##  print("Something else went wrong")

#2. else

##try:
##  print(x)
##except:
##  print("Something went wrong")
##else:
##  print("Nothing went wrong")

#3. finally

##try:
##  print(x)
##except:
##  print("Something went wrong")
##finally:
##  print("The 'try except' is finished")

#4. nested


##try:
##    f = open("D:\\demofile.txt", 'w')
##    try:
##        f.write("Lorum Ipsum")
##    except:
##        print("Contents were written to the to the file")
##    finally:
##        f.close()
##except:
##    print("Something went wrong when opening the file")
##
##try:
##    f = open("D:\\demofile.txt", 'r')
##    data = f.read()
##    print(data)
##except:
##    print("Something went wrong reading the file")

# 5. Raising exception

##x = -1
##
##if x < 0:
##  raise Exception("Sorry, no numbers below zero")

#6. Type exception

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

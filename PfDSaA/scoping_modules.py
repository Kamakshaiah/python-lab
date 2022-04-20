x = 4
y = 6
 
def outer_fun():
    global x
    x = 2
    y = 8
    def inner_fun():
        global x
        x = 3
        y = 7
        print('x inside inner_fun :', x)
        print('y inside inner_fun :', y)
    inner_fun()
    print('x inside outer_fun :', x)
    print('y inside outer_fun :', y)
     
outer_fun()
print('x outside all functions :', x)
print('y outside all functions :', y)

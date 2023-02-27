def MapDemo(i, j):
    ''' Utility function for map function. @i: list, @j: numeric value. '''
    
    return {'input': i, 'output': list(map(lambda i: i +j, i))}
                
def FilterDemo(i, c=None):
    ''' Utility function for filter function. @i: list, @c: condition '''
    return list(filter(lambda i: (eval(c)), i))

def ReduceDemo(i, oper=None):
    ''' Utility function for reduce demo. @i: list. '''
    import functools
    if oper=='add':
        return functools.reduce(lambda x, y: x + y, i)
    elif oper=='subtract':
        return functools.reduce(lambda x, y: x - y, i)
    elif oper=='multiply':
        return functools.reduce(lambda x, y: x * y, i)
    elif oper=='divide':
        return functools.reduce(lambda x, y: x / y, i)
    else:
        return "It's Okay"

def Sum(x):
    ''' Sum up the values of @x '''
    s_ = 0
    for i in x:
        s_ += i
    return s_

def Prod(x):
    ''' Multiply the elements of @x '''
    p_ = 1
    for i in x:
        p_ *= i
    return p_

def SquareArea(x):
    ''' Calculates area of a square for @x: side '''
    return x**2

def SquarePerimeter(x):
    ''' Calculates permiter of a square for @x: side '''
    return 4*x

def RectangleArea(l,b):
    ''' Calculates area of a rectangle for @l: leangth, @b: breadth. '''
    return l*b

def RectanglePerimeter(l, b):
    ''' Calculates perimeter of a rectangle for @l: leangth, @b: breadth. '''
    return 2*(l*b)

def CircleArea(r):
    ''' Calculates area of a circle for @r: radius. '''
    return 3.14*(r**2)

def CircleCircumference(r):
    ''' Calculates circumference of a circle for @r: radius. '''
    return 2*3.14*r

def TriangleArea(b, h):
    ''' Calculates area of a triangel for @b: base, @h: height '''
    return 0.5*b*h

def TriangePerimeter(*args, **kwargs):
    ''' Calculates area of 
        equilateral triangle: @s: side
        isosceles triangle: @s: side, @b: base
        scalene triangle: @s: list of sides. '''

    for k in kwargs:
        if k=='t':
            if k=='equil':
                for arg in args:
                    return 3*arg
            
            

if __name__ == '__main__':
##    print(Sum(range(1, 10)))
##    print(Prod([1, 2, 3, 4, 5]))
##    print(MapDemo(range(1, 10), 2))
##    print(FilterDemo(range(1, 10), c='i >3'))
##    print(ReduceDemo(range(1, 10), oper='hi'))
    print(TriangePerimeter(2, t='equil'))

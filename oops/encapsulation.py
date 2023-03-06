class computer:

    def __init__(self, price):
        self.__maxprice = price

    def getPrice(self):
        return self.__maxprice

    def setPrice(self, price):
        self.__maxprice = price

class triangle:

    def __init__(self, _type):
        self.__type = _type

    def info(self):
        return self.__type

if __name__ == '__main__':
    c = computer(1000)
    print(c.getPrice())
    c.__maxprice = 2000
    print(c.getPrice())
    c.setPrice(2000)
    print(c.getPrice())

##    t = triangle('isosceles')
##    print(t.info())
##    t.__type = 'equilaternal'
##    print(t.info())
        

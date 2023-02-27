class Computer:
    _name = 'Basic'
    
    def __init__(self):
        self._maxprice = 1000
        print('{} is ready'.format(self._name))

    def getMaxPrice(self):
        return self._maxprice

    def setMaxPrice(self, price):
        self._maxprice = price

class HpC(Computer):
    _name = 'HP'

    def __init__(self):
        super().__init__()
    

if __name__ == '__main__':
    c = Computer()
    print(c._maxprice)
    c._maxprice = 2000
    print(c._maxprice)
    c.setMaxPrice(3000)
    print(c._maxprice)
    print(c.getMaxPrice())
    hpc=HpC()
    print(hpc.getMaxPrice())
    hpc.setMaxPrice(5000)
    print(hpc.getMaxPrice())
                            


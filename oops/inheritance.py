class base:
    def __init__(self):
        print('base class created')

    def info(self):
        print('base')

    
class child1(base):
    
    def __init__(self):
        print('child class created')

    def info(self):
        print('child')


if __name__ == '__main__':
    b = base()
    c = child1()
    b.info()
    c.info()

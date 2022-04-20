class A:
    a = 'this is message from class A'
    def printinfo(self):
        print(self.a)

class B(A):
    pass

class C(B):
    a = 'this is a C level variable'
    
    @classmethod
    def cFunction(cls):
        A.a = "a is set from C"
    def cPrint(self):
        print(self.a)
        print(A.a)

if __name__ == '__main__':
    aObj = A()
    aObj.printinfo()
    bObj = B()
    bObj.printinfo()
    cObj = C()
    cObj.printinfo()
    cObj.cFunction()
    cObj.cPrint()
    print(aObj.a)

class arithmetic:

    def __init__(self, a=None, b=None):
        self.a = a if a is not None else 0
        self.b = b if b is not None else 0

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a/self.b

class hybrids(arithmetic):

    def __init__(self, a=None, b=None):
        super().__init__(a=None, b=None)
        

    def VecProd(self, vec=None):
        self.vec = vec if vec is not None else list()
        out = [i**2 for i in self.vec]
        return out

    def VecDiv(self, n):
        self.n = n
        out = [i/self.n for i in self.vec]
        return out

class descriptives:

    def __init__(self, vec):
        self.vec = vec
        self.summary = [max(vec), min(vec)]

    def mean(self):
        return (sum(self.vec)/len(self.vec))
    
    def median(self):
        n = len(self.vec)
        if n%2 == 0:
            med1 = self.vec[n//2]
            med2 = self.vec[n//2 - 1]
            return (med1 + med2)/2
        else:
            return(self.vec[n//2])

    def moment(self, n):
        out = sum([i - self.mean()**n for i in self.vec])
        return out/len(self.vec)

    def var(self):
        numer = sum([(i - self.mean())**2 for i in self.vec])
        return numer/len(self.vec)

    def std(self):
        out = self.var()**0.5
        return out

    def skewness(self):
        m3 = self.moment(3)
        out = m3/(self.std()**3)
        return out
        
    def kurtosis(self):
        m3 = self.moment(4)
        out = m3/(self.std()**4)
        return out

    def makeHist(self):
        import matplotlib.pyplot as plt
        from scipy.stats import norm
        import numpy as np
        
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, len(self.vec))    
        p = norm.pdf(x, self.mean(), self.std())

        plt.hist(self.vec)
        plt.plot(x, p)

        plt.show()
        
class Customer:

    custype = 'ordinary'
    
    def __init__(self, first, last, pamt):
        self.first = first
        self.last = last
        self.pamt = pamt
        self.fulname = '{} {}'.format(self.first, self.last)
        self.credits = self.Credit(pamt)
        self.custype = self.customerType(pamt) 
        
    def Credit(self, pamt):
        if self.pamt > 1000:
            return self.pamt * 0.05
        elif self.pamt > 500 and self.pamt <= 1000:
            return self.pamt * 0.10
        
    def customerType(self, pamt):
        if self.pamt > 10000:
            return 'extradinary'
        elif self.pamt > 1000 and self.pamt <= 10000:
            return 'premium'
        else:
            return self.custype

class bestCustomer(Customer):

    def __init__(self, first, last, pamt, freq):
        super().__init__(first, last, pamt)
        self.freq = freq
        self.disc = self.Discount(self.pamt, self.freq)

    def Discount(self, pamt, freq):
        if self.freq > 50 and self.pamt >= 10000:
            return self.pamt * 0.20
        else:
            return '''Discount not applicable'''
        
    


    

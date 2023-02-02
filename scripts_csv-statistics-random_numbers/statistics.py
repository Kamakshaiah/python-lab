class Statistics:

    __help = ''' This package is useful to compute statistics '''

    def help(self):
        return('A module to help perform statistics')
        
    def mean(self, vec):
        ''' Return arithmetic mean of sample distribution '''
        numer = sum(vec)
        denom = len(vec)
        return (numer/denom) 

    def median(self, vec):
        ''' Returns median of sample distribution '''
        if len(vec)%2 == 0:
            med1 = vec[len(vec)//2]
            med2 = vec[len(vec)//2 - 1]
            return (med1 + med2)/2
        else:
            return vec[len(vec)//2]

    def mode(self, vec):
        ''' Returns mode of the sample distribution '''
        from collections import Counter
        n = len(vec)
        data = Counter(vec)
        getDat = dict(data)
        mode = [k for k, v in getDat.items() if v == max(list(data.values()))]
        if len(mode) == n:
            print('No mode found')
        else:
            return mode

class Dispersion:

    __help = ''' Return Variance and Skewness '''

    def __init__(self):
        self.mean = Statistics.mean

    def Variance(self, vec):
        ''' Returns variance of the distribution '''
        numer = sum([(i-self.mean(vec))**2 for i in vec])
        denom = len(vec)

        return numer/denom

    def StanDev(self, vec):
        ''' Returns Standard Deviation of the distribution '''
        return self.Variance(vec)**0.5
        

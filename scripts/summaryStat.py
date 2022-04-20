class summaries:

    def __init__(self, vec):
        
        self.vec = vec

    def mean(self):
        ''' computes mean '''
        return (sum(self.vec)/len(self.vec))

    def median(self):
        ''' computes median '''
        n = len(self.vec)//2 
        if  n%2 == 0:
            m1 = self.vec[n//2]
            m2 = self.vec[n//2 - 1]
            return (m1 + m2)/2
        else:
            return (self.vec[n//2])

    def mode(self):
        ''' computes mode '''
        from collections import Counter

        data = Counter(self.vec)
        datDic = dict(data)

        mode = [k for k,v in datDic.items() if v == max(list(data.values()))]
        if len(mode) == len(self.vec):
            print('No mode found')
        else:
            return mode

    
    class Dispersion:

        

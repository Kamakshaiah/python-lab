class gs:
    ''' extracts material from Google Scholar '''

    def __init__(self, q, hl='en', as_ylo=0, num=10):
        self.q = q
        self.hl = hl
        self.as_ylo=as_ylo
        self.num=num

    def makeQuery(self):
        return 'https://scholar.google.com/scholar?'+'hl='+self.hl+'&'+'q='+self.q+'&'+'as_ylo='+str(self.as_ylo)+'&'+'num='+str(self.num)
    

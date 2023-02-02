class gs:
    ''' extracts material from Google Scholar '''
    hv = ['am', 'is', 'are', 'was', 'and', 'were', 'being', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
          'may', 'might', 'must', 'can', 'could', 'of', 'for', 'about', 'with', 'on', 'inside', 'under', 'lower', 'upper', 'a', 'an', 'the', 'in', 'new',
          'old', 'through', 'suitable', 'suiit']
          
    def __init__(self, q, hl='en', as_ylo=0, num=10):
        self.q = q
        self.hl = hl
        self.as_ylo=as_ylo
        self.num=num

    def makeQuery(self):
        ''' create the url for google sholar search '''
        return 'https://scholar.google.com/scholar?'+'hl='+self.hl+'&'+'q='+self.q+'&'+'as_ylo='+str(self.as_ylo)+'&'+'num='+str(self.num)
    

    def getLinks(self, url):
        
        from bs4 import BeautifulSoup
        import requests
        import random
        

        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
               )
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        alinks = soup.findAll('a')

        links = []

        for a in alinks:
            if 'google' in a.get('href'):
                next
            elif 'https://' in a.get('href'):
                links.append(a.get('href'))

        return links        

    def openSource(self, links, **kwargs):

        ''' opens the link '''

        import webbrowser as wb
        
        if 'num' in kwargs.keys():
            arg1 = kwargs['num']
            wb.open(links[arg1])
        elif 'allsources' in kwargs.keys():
            for i in links:
                wb.open(i)

    def getAbstract(self, links, num = 1):
        ''' get abstract for given page source '''

        from bs4 import BeautifulSoup
        import requests
        import random

        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36")
        
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}

        ps = requests.get(links[num], headers=headers)
        soup = BeautifulSoup(ps.content, 'lxml')
        ptags = soup.find_all('p')

        abs = ['abstract', 'Abstract', 'ABSTRACT']

        for p in ptags:
            for i in abs:
                if i in p.text:
                    print(p.text)
                    
    def getTitles(self, url):
        ''' retrieves titles '''

        from bs4 import BeautifulSoup
        import requests
        import random
        

        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
               )
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        heads = soup.findAll('h3')

        titles = []

        for t in heads:
            titles.append(t.text)

        return titles

    def wordFrequencies(self, titles):
        ''' makes word frequencies '''

        text = ''

        for t in titles:
            text += t

        wordlist = text.split()
        wordfreq = []

        for w in wordlist:
            wordfreq.append(wordlist.count(w))
            
        wordlist1 = []
        for i in wordlist:
            wordlist1.append(i.lower())

        return {'wordslist': wordlist1, 'wordfreq': wordfreq}

    def makeDistinctWords(self, title, termmat, length=7):

        ''' creates words and frequenceis '''

        words = []
        freq = []
        titlewords = title.split()

        for i, j in zip(termmat['wordslist'], termmat['wordfreq']):
            if i in self.hv:
                next
            elif i in titlewords:
                next
            elif len(i) < length:
                next
            else:
                words.append(i)
                freq.append(j)
                
        return {'words': words, 'freq': freq}

    def barChart(self, termmat):

        ''' creates barchart for termmat '''

        import matplotlib.pyplot as plt
        plt.bar(distinctwords['words'], distinctwords['freq'])
        plt.xticks(rotation=45)
        plt.show()
        
##if __name__ == '__main__':
##    title = 'internet of things for smart cities'
##    gscholar = gs(title)
##    url = gscholar.makeQuery()
##    print(url)
##    links = gscholar.getLinks(url)
##    print(links) 
##    print(len(links))
##
##    for i in links:
##        print(i) 
##    gscholar.openSource(links, num=7)
##    gscholar.getAbstract(links, num=7)
##    titles = gscholar.getTitles(url)
##    for i in titles:
##        print(i)
##    termmat = gscholar.wordFrequencies(titles)
##    print(termmat)
##    distinctwords = gscholar.makeDistinctWords(title, termmat)
##    print(distinctwords)
##    gscholar.barChart(distinctwords)

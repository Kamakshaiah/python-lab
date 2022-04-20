class gScholar:

    ''' Extracts material from Google Scholar. Supports few methods such as
            - retrieval of links
            - retrieval of titles
            - creats termmat (word-freq matrix)
            - create distinct words matrix (with unique words)
            - support statistical analysis
                - IQR
                - Two Sample T Test
                - Moods Test of Sample Medians
                - Cluster analysis
        Apart from the above methods; supports few utility functions such as:
            - creating tables for (termat, disctinct words, etc...)
            - saves tables in given paths '''

    hv = ['am', 'is', 'are', 'was', 'and', 'were', 'being', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
          'may', 'might', 'must', 'can', 'could', 'of', 'for', 'about', 'with', 'on', 'inside', 'under', 'lower', 'upper', 'a', 'an', 'the', 'in', 'new',
          'old', 'through', 'suitable', 'suiit']
          
    def __init__(self, q, hl='en', startyear=0, num=10):
        self.q = q
        self.hl = hl
        self.as_ylo=startyear
        self.num=num

    def makeQuery(self):
        ''' Create the url for google sholar search '''
        
        return 'https://scholar.google.com/scholar?'+'hl='+self.hl+'&'+'q='+self.q+'&'+'as_ylo='+str(self.as_ylo)+'&'+'num='+str(self.num)
    

    def getLinks(self, url):

        ''' retrieves links for search phrase '''
        
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
        soup = BeautifulSoup(r.content, "html.parser")
        alinks = soup.findAll('a')

        links = []

        for a in alinks:
            if 'google' in a.get('href'):
                next
            elif 'https://' in a.get('href'):
                links.append(a.get('href'))

        return links        

    def getTitles(self, url):
        ''' Retrieves titles '''

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
        soup = BeautifulSoup(r.content, "html.parser")
        heads = soup.findAll('h3')

        titles = []

        for t in heads:
            titles.append(t.text)

        return titles


    def openLink(self, links, **kwargs):

        ''' Opens the given link '''

        import webbrowser as wb
        
        if 'num' in kwargs.keys():
            arg1 = kwargs['num']
            wb.open(links[arg1])
        elif 'allsources' in kwargs.keys():
            for i in links:
                wb.open(i)

    def getText(self, links, path, num, savetext=False):
        ''' Get abstract for given page source. No support for PDF files '''

        from bs4 import BeautifulSoup
        import requests
        import random

        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36")
        
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}

        ps = requests.get(links[num], headers=headers)
        soup = BeautifulSoup(ps.content, "html.parser")
        ptags = soup.find_all('p')

        abs = ['abstract', 'Abstract', 'ABSTRACT']

        text = ''
        
        for p in ptags:
            print(p.text)

        if savetext==True:
            for p in ptags:
                text += p.text + '\n'

        path = path + '\\file.txt'

        f = open(path,'w')
        f.write(text)
        f.close()            
                    
            
if __name__ == '__main__':
    title = 'solar power plant performance'
    path = 'D:\\Work\\Python\\Scripts\\literature-review-mainone\\'
    gs = gScholar(title, startyear=2020, num=30)
    url = gs.makeQuery()
    print(url)
    links = gs.getLinks(url)
    print(len(links))
##
##    for i in links:
##        print(i) 
##    gs.openLink(links, num=7)
##    gs.getText(links, path=path, num=15,  savetext=True)
    titles = gs.getTitles(url)
    for i in titles:
        print(i)
##    termmat = gs.wordFrequencies(titles)
##    print(termmat)
##    ttbl = gs.makeTables(termmat)
##    pathch = path + 'termmat.csv'
##    gs.saveAsCSVFile(pathch, ttbl)
##    distinctwords = gs.makeDistinctWords(title, termmat)
##    print(distinctwords)
##    gs.barChart(distinctwords)
##    dwtbl = gs.makeTables(distinctwords)
##    gs.boxPlot(dwtbl)
##    pathch = path + 'dwtbl.csv'
##    gs.saveAsCSVFile(pathch, dwtbl)
##    gs.twoSampleIndTTest(termmat['wordfreq'], distinctwords['freq']) # this test can be used for two different searches
    
##    print(gs.computeIQR(dwtbl['freq']))
##    wordvec = gs.reshapeData(distinctwords)
##    nc = 2
##    clssol = gs.clusterAnalysis(distinctwords, path, nc=3, output=True) # saves the output 
##    print(clssol) 
##    pathch = path + 'out.csv'
##    cluswords = gs.wordsByCategory(pathch, 2) # reads data from fs
##    gs.pieForCategories(cluswords)
##    print(gs.crosstabFromWordsMatrix(pathch, output=True, norm=True)) # reads data from fs and then makes cross tab
    
    

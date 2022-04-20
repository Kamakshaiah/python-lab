class gSearch:

    ''' Performs google search and retrieves words '''

    def __init__(self, title, num_links=10, duration=1):

        self.q = title
        self.num_links = num_links
        self.duration = duration

        self.google_url = f"https://www.google.com/search?q={title}" + f"&num={str(num_links)}" + f"&as_qdr=y{duration}"

    def getUrl(self):

        ''' Returns url for google search '''

        return self.google_url

    def getTitlesAndLinks(self):

        ''' Retrieves titles and links for search title '''

        import requests
        
        from my_fake_useragent import UserAgent
        from bs4 import BeautifulSoup

        ua = UserAgent()

        r = requests.get(self.google_url, {"User-Agent": ua.random})

        soup = BeautifulSoup(r.content, 'lxml')

        titles = soup.find_all('h3')

        titlesout = []
        for t in titles:
            titlesout.append(t.text)

        alinks = soup.findAll('a')
        alinksout = []
        
        for l in alinks:
            alinksout.append(l.get('href'))

        links = []

        for l in alinksout:
            if not 'google' in l and '/url?q=' in l:
                links.append(l)
        
        return {'titles': titlesout, 'links': links}

    @staticmethod
    def getLinks(links):

        ''' Removes '/url?q=' in the links '''

        linksget = []

        for l in links:
            linksget.append(l.replace('/url?q=', ''))

        linksfinal = []
        for l in linksget:
            linksfinal.append(str.partition(l, '&')[0])
            
        return linksfinal
            

    @staticmethod
    def openLink(links, **kwargs):
        
        ''' Opens the given link inside browser tab for two arguments (1) links (2) num/allsources'''

        import webbrowser as wb
        
        if 'num' in kwargs.keys():
            arg1 = kwargs['num']
            wb.open(links[arg1])
        elif 'allsources' in kwargs.keys():
            for i in links:
                wb.open(i)
                
    @staticmethod
    def saveTextFromLinks(links, path, link_num=0, name='name.txt'):

        ''' Scrapes text from given links (for link_num=0, name='name.txt') and saves the text in 'path' for further analysis '''
        
        import os
        import requests
        from bs4 import BeautifulSoup
        from my_fake_useragent import UserAgent
        ua = UserAgent()
        
        ps = requests.get(links[link_num], {"User-Agent": ua.random})

        soup = BeautifulSoup(ps.content, 'lxml')
        ptags = soup.find_all('p')

        text = ''
        
        for p in ptags:
            text += p.text + '\n'
        

        if os.path.exists('output'):
            path = path + 'output\\' + name
        else:
            os.mkdir('output')
            path = path + 'output\\' + name

        f = open(path,'w', encoding='utf-8')
        f.write(text)
        f.close() 


##if __name__ == '__main__':
##
##    title = 'impact of spirituality and religious practices during Covid-19'
##    num_links = 10
##    duration = 1
##    
##    gs = gSearch(q = title, num_links=num_links, duration=duration)
##
##    print(gs.getUrl())
##    titles = gs.getTitlesAndLinks()['titles']
##    links = gs.getTitlesAndLinks()['links']
##
##    linksch = gs.getLinks(links)
##
##    
    
    

    

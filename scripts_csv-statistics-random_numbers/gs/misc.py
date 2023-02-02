##import urllib.request
##
##url = 'https://google.com/search?q=Where+can+I+get+the+best+coffee'
##
### Perform the request
##request = urllib.request.Request(url)
##
### Set a normal User Agent header, otherwise Google will block the request.
##request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
##raw_response = urllib.request.urlopen(request).read()
##
### Read the repsonse as a utf-8 string
##html = raw_response.decode("utf-8")
##
##from bs4 import BeautifulSoup
##
### The code to get the html contents here.
##
##soup = BeautifulSoup(html, 'html.parser')
##
### Find all the search result divs
##divs = soup.select("#search div.g")
##for div in divs:
##    # Search for a h3 tag
##    results = div.select("h3")
##
##    # Check if we have found a result
##    if (len(results) >= 1):
##
##        # Print the title
##        h3 = results[0]
##        print(h3.get_text())

import requests
from bs4 import BeautifulSoup
import random
 
text = 'python'
url = 'https://scholar.google.com/scholar?en&'+text+'&0&10'
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]
 
headers = {'user-agent': Agent}
r = requests.get(url, headers=headers)
 
soup = BeautifulSoup(r.text, 'lxml')
for info in soup.find_all('h3'):
    print(info.text)

####    print('#######')
##
##import requests
##from bs4 import BeautifulSoup
##import random
## 
##url = 'python'
##A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
##       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
##       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
##       )
## 
##Agent = A[random.randrange(len(A))]
## 
##headers = {'user-agent': Agent}
##r = requests.get(url, headers=headers)
## 
##soup = BeautifulSoup(r.content, 'lxml')
##
####title = soup.find('title')
####print("Title of the webpage--\n")
####print(title.string)
##search = soup.find_all('div',class_="site")
##print("Hyperlink in the div of class-site--\n")
##for h in search:
##    print(h.a.get('href')) 


def appendText(path):
    
    ''' Append text inside text files at given path. Makes a master output file concatinating all the text inside text (.txt) files '''
    
    import os

    filenames = os.listdir(path)
    
    with open(path, 'w', encoding='utf-8') as outfile:
        for f in filenames:
            with open(os.path.join('output\\' + f), 'r', encoding='utf-8') as infile:
                contents = infile.read()
                contents.encode('utf-8')
                outfile.write(contents)
                infile.close()
        outfile.close()

def wordCounts(wwov):

    ''' Count (google search list) WORDS and creates a dictinary of words and frequencies (termmat)
        wwov - words with out verbs (obtained from google search module) '''

    wordlist = wordstring.split()

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    return {'words': wordlist, 'freq': wordfreq}



def wordFrequencies(titles):
    ''' Makes word frequencies with (google scholar) TITLES and frequencies as dictionary (ref. to termmat - term matrix) '''

    import re
    
    text = ''

    for t in titles:
        text += t

    wordlist = text.split()
    
    wordlist1 = []
    for i in wordlist:
        wordlist1.append(re.sub('[^A-Za-z0-9]', ' ', i.lower()))

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist1.count(w))
    
    return {'words': wordlist1, 'freq': wordfreq}


def makeDistinctWords(title, termmat, length=7):

    ''' Creates words and their respective frequenceis for termmat (compares titles to its search string)
        Makes disctinct words matrix - (disctinctwords) '''

    words = []
    freq = []
    titlewords = title.split()

    idx[0] = termmat.keys()[0]
    idx[1] = termmat.keys()[1]
    
    for i, j in zip(termmat[idx[0]], termmat[idx[1]]):
        if i in self.hv:
            next
        elif i in titlewords:
            next
        elif len(i) < length:
            next
        else:
            words.append(i)
            freq.append(j)

    if words:
        words_new = []
        freq_new = []
        for i, j in zip(words, freq):
            if i not in words_new:
                words_new.append(i)
                freq_new.append(j)
                            
    return {'words': words_new, 'freq': freq_new}


def makeTables(data):
    ''' Creates tablar data for distinctwords (dictionary) or termmat (dictionary) '''
    
    import pandas as pd

    tbl = pd.DataFrame(data)
    return tbl


def saveAsCSVFile(path, data):
    ''' Converts pandas DF (tables) to csv file and saves in the request path (arg: path)'''
    data.to_csv(path)

    
    

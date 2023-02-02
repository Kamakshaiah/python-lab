# divide the text into sentences

import nltk
nlkt.downlaod('punkt')
text = "Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger. Sanger coined its name[5][6] as a portmanteau of 'wiki' and 'encyclopedia'. It was initially an English-language encyclopedia, but versions in other languages were quickly developed. With 6.2 million articles, the English Wikipedia is the largest of the more than 300 Wikipedia encyclopedias. Overall, Wikipedia comprises more than 55 million articles,[7] attracting 1.7 billion unique visitors per month.[8][9]"
textlist = nltk.tokenize.sent_tokenize(text)
import os
os.getcwd()
os.chdir('D:\\work\\python_work\\scripts')
import csv
with open('qns.csv', 'w') as f:
	qns = csv.writer(f)
        for row in [textlist]:
            qns.writerows(row)

# ---- other simple approach ---- #

##import re
##text = ''.join(open('somefile.txt').readlines())
##sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

import re
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
# now sentences has required rows

# finding sentences with required answers

answers = ['Wikipedia', 'portmanteau', 'encyclopedia']
qns = []

for (row, word) in zip(textlist, answers):
	if word in row:
		qns.append(row.replace(word, '[          ]'))

with open('qns.csv', 'w') as f:
	mcqs = csv.writer(f)
	for (row, word) in zip(qns, answers):
		mcqs.writerow([[row], word])

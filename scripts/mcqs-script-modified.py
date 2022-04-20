import re
import os
import csv

path = 'D:\\work\\python_work\\scripts'
text = 'The number of edtech entrepreneurs is steadily rising in India. The top Indian edtech companies market has been a promising one, as it provides immensely profitable opportunities in return for nation-building services. The prospects are set to increase as the education sector is evolving.'

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
# now sentences has required rows

# finding sentences with required answers

answers = [' edtech', 'promising', 'education sector']
qns = []

for (row, word) in zip(sentences, answers):
	if word in row:
		qns.append(row.replace(word, '[          ]'))
pathupdated = str(path + '\\qns.csv')

with open(pathupdated, 'w') as f:
	mcqs = csv.writer(f)
	for (row, word) in zip(qns, answers):
		mcqs.writerow([row, word])

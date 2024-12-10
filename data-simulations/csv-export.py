import os
os.getcwd()
'C:\\Program Files\\Python311'
os.chdir('D:\\Miscel\\python')
os.getcwd()
'D:\\Miscel\\python'
import random as rnd

var1 = rnd.sample(range(1, 12), 10)
var2 = rnd.sample(range(1, 12), 10)

l = list([var1, var2])
rows_ = list(zip(*l))

with open('dataset.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerows(rows_)

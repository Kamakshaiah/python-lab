# https://realpython.com/python-csv/

# data = np.loadtxt('D:\\Miscel\\dataset.csv',delimiter=',')
# data = np.genfromtxt('D:\\Miscel\\dataset.csv', delimiter=',') # works but data will be buggy

data = np.recfromcsv('D:\\Miscel\\dataset.csv', encoding='utf-8', delimiter=',')

data.size
data.ndim

data[0] # first row
type(data[0]) # <class 'numpy.record'>

data[:5,] # head
data[:5,][1] # first row
data[:5,][0][0] # data point in first row first column

# first column
for i in range(data.size):
    for j in range(data[i].size):
        print(data[i][j])

# other formats
## numpy

import csv
with open('D:\\Miscel\\dataset.csv', encoding='utf-8') as file:
    data = list(csv.reader(file))
    print(data) # prints csv.reader object

with open('D:\\Miscel\\dataset.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    print([r for r in data]) # prints list (horizontal)

with open('D:\\Miscel\\dataset.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    for r in data:
        print(r) # prints list (vertical)

# pandas

data = pd.read_csv('data.csv', header=None)

data = data.to_numpy()
np.array(data)

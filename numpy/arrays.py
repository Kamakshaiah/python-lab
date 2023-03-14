import numpy as np

np.arange(10)
np.arange(10, 30)

np.arange(25).reshape(5, 5) # 5 X 5 matrix
np.arange(25, 50).reshape(5, 5)

np.array([1, 2, 3])
np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3) # 2X3 matrix

# indexing

array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) 
##array
array[0] # first row

for i in range(3):
    print(array[i][0])

array[1] # second row

for i in range(3):
    print(array[i][1])

array[0][1] # row 1 column 2 element

# colon notation
## left from right until
## array[from:until]

array[0:] # full array
array[1:] # from row 1
array[1:] # from row 2
array[:1] # only first row
array[:2] # until row row

## row column format

array[:, ] # full array
array[1:, ] # from second row
array[:, 1:] # from second column
array[:, :1] # until first column



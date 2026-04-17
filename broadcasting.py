import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])

# broadcasting --> means performing operations on arrays of different shapes without making copies of data. It "stretches" smaller arrays to match the shape of larger ones — conceptually, not literally in memory.

print(array1 + array2) # we can add, subtr, multiply & divide
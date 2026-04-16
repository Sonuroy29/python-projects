import numpy as np

# scalar arithmetic :-

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + 2) # addition
print(array1 - 2) # subtraction
print(array1 * 2) # multiply
print(array1 / 2) # divide
print(array1 ** 2) # raised to the power


# vectorized math functions :-

print(np.sqrt(array1)) # square root
print(np.round(array1)) # rounding off
print(np.floor(array1)) # round down
print(np.ceil(array1)) # round up
print(np.pi) # constant --> pi


# element wise arithmetic :-

print(array1 + array2) # add
print(array1 - array2) # subtr
print(array1 * array2) # multiply
print(array1 / array2) # divide


# comparison operators :- return results in boolean form

scores = np.array([100, 95, 90, 65, 50, 46, 36, 20])

print(scores == 100)
print(scores >= 50)
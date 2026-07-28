import numpy as np

arr = np.array([3, 12, 7, 45, 9, 22, 8, 14])
print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())

#Create a new array containing only values greater than
arr_greater_10 = arr[arr > 10]

#Create a new array where every value is doubled (using vectorized multiplication, not a loop).
arr_doubled = arr * 2

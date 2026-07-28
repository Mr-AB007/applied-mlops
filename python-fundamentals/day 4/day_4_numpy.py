import numpy as np

#Array using numpy

arr = np.array([1, 2, 3])
zeros = np.zeros_like(arr)
ones = np.ones_like(arr)
arr_range = np.arange(0,10,2) #start ,stop ,step

#print(arr_range)

#Vectorized operations

arr_doubled = arr*2
arr_squared = arr**2
arr_sum = arr + 10

#Useful array operations

arr = np.array([3, 12, 7, 45, 9, 22,10])

sum = arr.sum()        # 98
mean = arr.mean()      # 16.33
max = arr.max()        # 45
min = arr.min()        # 3
arr_sorted = arr.sort()       # sorts in place
arr_greater10 = arr[arr < 10] # filtering: [12 45 22] — array of elements matching condition

#2D array

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_2d)
# print(arr_2d.shape)
# print(arr_2d[0][1])
#print(arr_2d[:,1])  # column 1 across all rows -> [2 5]



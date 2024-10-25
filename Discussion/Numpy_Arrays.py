import numpy as np

# Adding arrays together

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = arr1 + arr2

# Appending arrays

arr4 = np.append(arr1, arr2)
print(arr4)

# Indexing 1D Arrays

arr5 = arr4[2:]
print(arr5)

# Other functions

print(np.sum(arr4))
print(np.std(arr4))

# Practice Problem

total_sum = 0
for i in range(1, 101):
    total_sum += i
print(total_sum)

print(np.sum(range(1, 101)))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix.shape)
print(matrix[1, 1])
print(np.linalg.det(matrix))
import numpy as np

# Create a m x n matrix of zeros
m, n = 3, 3
matrix = np.zeros(shape=(m, n), dtype=int)

# Fill diagonal with 1's
for i in range(m):
    for j in range(n):
        if (i == j):
            matrix[i, j] = 1

print(matrix, '\n')

# Fill non-diagonal with 3's
for i in range(m):
    for j in range(n):
        if (i != j):
            matrix[i, j] = 3

print(matrix, '\n')

# Delete last column
matrix = np.delete(matrix, n-1, 1)
print(matrix)

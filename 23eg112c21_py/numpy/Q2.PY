import numpy as np
# this is for random numbers
# matrix_random = np.random.randint(1, 17, size=(3, 3))
# print("Matrix with random values:\n", matrix_random)

# now we will create matrix of size 4,4 with numbers from 1 to 16 in order
matrix = np.arange(1, 17).reshape(4, 4)
print("Matrix with values from 1 to 16:\n", matrix)
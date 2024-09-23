import numpy as np

m1 = np.random.randint(1, 17, size=(3, 3))
m2 = np.random.randint(1, 17, size=(3, 3))
# print(m1)
# print(m2)

# matrix multiplication
result = np.dot(m1, m2)
print(result)

# matrix addition
summ = np.add(m1, m2)
# print(summ)

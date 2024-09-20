import numpy as np

m = np.random.randint(1,10,size=(3,3))

print(m)
print("row wise sum of matrix is: ", np.sum(m, axis=1))
print("column wise sum of matrix is: ", np.sum(m, axis=0))
import numpy as np

a = np.array([4, 5, 6, 3, 2, 3, 4, 2, 4, 6, 4, 6, 7, 7, 7, 3, 4, 4])
unique, counts = np.unique(a, return_counts=True)
frequency_dict = dict(zip(unique, counts))

for key, value in frequency_dict.items():
    print(f"{key} - {value}")

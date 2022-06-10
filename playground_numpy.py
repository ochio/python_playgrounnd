import numpy as np

x = np.array([[1, 2], [3, 4]])
x = x.flatten()
print(x[x > 2])

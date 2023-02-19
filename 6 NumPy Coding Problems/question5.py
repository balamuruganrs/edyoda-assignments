# 5) Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

arr = np.random.random((10 , 10))
mini = arr.min()
maxi = arr.max()
print(arr)
print("minimum number : ",mini)
print("maximin number : ",maxi)
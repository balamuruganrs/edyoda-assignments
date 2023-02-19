# 4) Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

arr = np.array([1,2,0,0,4,0])
non_zero = np.nonzero(arr)
print(non_zero)
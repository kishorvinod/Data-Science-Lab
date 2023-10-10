import numpy as np
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")

arr1d = np.array([1, 2, 3, 4, 5])
inserted_arr = np.insert(arr1d, 2, 6)

print("Original 1D Array:")
print(arr1d)

print("\n1D Array after Insertion:")
print(inserted_arr)

import numpy as np


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

inserted_arr = np.insert(arr2d, 1, [10, 11, 12], axis=0)

print("Original 2D Array:")
print(arr2d)

print("\n2D Array after Insertion:")
print(inserted_arr)


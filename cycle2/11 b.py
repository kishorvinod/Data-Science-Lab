import numpy as np
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

Y = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

result = np.power(X, 2) + 2 * Y

print("Matrix X:")
print(X)

print("\nMatrix Y:")
print(Y)

print("\nResult of X^2 + 2Y:")
print(result)

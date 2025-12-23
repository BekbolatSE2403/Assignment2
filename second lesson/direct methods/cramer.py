import numpy as np

def cramer(A, b):
    n = len(A) 
    D = np.linalg.det(A)

    x = np.zeros(n)
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        D_i = np.linalg.det(A_i)
        x[i] = D_i / D

    return x


A = np.array([[2, 3], [4, 1]])
b = np.array([5, 11])
x_cramer = cramer(A, b)
print(f"Solution: {x_cramer}")
print(f"Exact: [2.8, -0.2]\n")
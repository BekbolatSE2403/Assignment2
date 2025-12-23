import numpy as np

def gauss_jordan(A, b):
    n = len(A)
    aug = np.hstack([A.astype(float), b.reshape(-1, 1)])
    
    for k in range(n):
        max_row = np.argmax(np.abs(aug[k:, k])) + k
        if max_row != k:
            aug[[k, max_row]] = aug[[max_row, k]]
        
        pivot = aug[k, k]
        aug[k, :] = aug[k, :] / pivot
        
        for i in range(n):
            if i != k:
                factor = aug[i, k]
                aug[i, :] -= factor * aug[k, :]
    
    x = aug[:, -1]
    return x

A = np.array([[1, 1, 1],
              [2, -3, 4],
              [3, 4, 5]], dtype=float)
b = np.array([9, 13, 40], dtype=float)
x_gj = gauss_jordan(A, b)
print(f"Solution: {x_gj}")
print(f"Exact: [1, 3, 5]\n")
import numpy as np

def gaussian(A, b, partial_pivoting=False):
    n = len(A)
    aug = np.hstack([A.astype(float), b.reshape(-1, 1)])
    

    for k in range(n-1):
        if partial_pivoting:
            # Find row with maximum absolute value in column k
            max_row = np.argmax(np.abs(aug[k:, k])) + k
            if max_row != k:
                aug[[k, max_row]] = aug[[max_row, k]]
        
        # Eliminate below diagonal
        for i in range(k+1, n):
            factor = aug[i, k] / aug[k, k]
            aug[i, k:] -= factor * aug[k, k:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (aug[i, -1] - np.dot(aug[i, i+1:n], x[i+1:n])) / aug[i, i]
    
    return x

A = np.array([[1, 2, 1],
              [0, 2, 5],
              [3, 4, 1]], dtype=float)
b = np.array([4, 6, 7], dtype=float)
x_gauss = gaussian(A, b)
print(f"Solution: {x_gauss}")
print(f"Exact: [-0.6667, 2.1667, 0.3333]\n")
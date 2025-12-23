import numpy as np

def gauss_seidel_method(A, b, x0=None, max_iter=100, tol=1e-6):
    n = len(A)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    
    for iteration in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum_ax = 0
            for j in range(i):
                sum_ax += A[i, j] * x[j]
            for j in range(i+1, n):
                sum_ax += A[i, j] * x_old[j]
            
            x[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.linalg.norm(x - x_old) < tol:
            print(f"Gauss-Seidel converged in {iteration+1} iterations")
            break
    
    return x

A = np.array([[20, 1, -2],
              [3, 20, -1],
              [2, -3, 20]], dtype=float)
b = np.array([17, -18, 25], dtype=float)
x_gs = gauss_seidel_method(A, b, max_iter=10)
print(f"Solution: {x_gs}")
print(f"Exact: [1, -1, 1]\n")
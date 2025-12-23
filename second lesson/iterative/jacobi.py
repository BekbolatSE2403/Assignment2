import numpy as np

def jacobi_method(A, b, x0=None, max_iter=100, tol=1e-6):
    n = len(A)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    
    x_new = np.zeros(n)
    
    for iteration in range(max_iter):
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if j != i:
                    sum_ax += A[i, j] * x[j]
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.linalg.norm(x_new - x) < tol:
            print(f"Jacobi converged in {iteration+1} iterations")
            break
        
        x = x_new.copy()
    
    return x_new

A = np.array([[2, 1, 1],
              [1, 3, -1],
              [-1, 1, 2]], dtype=float)
b = np.array([6, 0, 3], dtype=float)
x_jacobi = jacobi_method(A, b, max_iter=20)
print(f"Approximate solution: {x_jacobi}")
print("(Exact: [1, -1, 3] after many iterations)\n")
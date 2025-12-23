import numpy as np

def relaxation_method(A, b, omega=1.2, x0=None, max_iter=100, tol=1e-6):
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
            
            gs_update = (b[i] - sum_ax) / A[i, i]
            x[i] = (1 - omega) * x_old[i] + omega * gs_update
        
        if np.linalg.norm(x - x_old) < tol:
            print(f"Relaxation (ω={omega}) converged in {iteration+1} iterations")
            break
    
    return x

A = np.array([[3, 1, -1],
              [1, 4, 1],
              [-1, 1, 5]], dtype=float)
b = np.array([3, 6, 7], dtype=float)
x_relax = relaxation_method(A, b, omega=1.2, max_iter=10)
print(f"Solution: {x_relax}")
print(f"Exact: [1, 1, 1]\n")
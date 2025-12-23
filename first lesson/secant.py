
import math

def f(x):
    return x**2 - 4 

x0 = 1.0  
x1 = 3.0 

for i in range(10): 
    f0 = f(x0)
    f1 = f(x1)
    
    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    error = abs(x2 - x1)
    
    print(f"Step {i+1}: x = {x2:.6f}, f(x) = {f(x2):.6f}, error = {error:.6f}")
    
    if error < 0.0001: 
        break
    
    x0, x1 = x1, x2

print(f"\nFinal answer: {x2:.6f}")
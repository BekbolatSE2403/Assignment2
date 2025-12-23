
import cmath 

def f(x):
    return x**2 - 4  

x0 = 1.0
x1 = 2.5
x2 = 3.0

for i in range(10): 
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    

    h1 = x1 - x0
    h2 = x2 - x1
    
    d1 = (f1 - f0) / h1
    d2 = (f2 - f1) / h2
    
    a = (d2 - d1) / (h2 + h1)
    b = a * h2 + d2
    c = f2
    
    disc = cmath.sqrt(b**2 - 4*a*c)
    denom1 = b + disc
    denom2 = b - disc
    
    if abs(denom1) > abs(denom2):
        x3 = x2 - (2*c) / denom1
    else:
        x3 = x2 - (2*c) / denom2
    
    error = abs(x3 - x2)
    
    print(f"Step {i+1}: x = {x3:.6f}, f(x) = {f(x3):.6f}, error = {error:.6f}")
    
    if error < 0.0001: 
        break
    
    x0, x1, x2 = x1, x2, x3
    

print(f"\nFinal answer: {x3:.6f}")
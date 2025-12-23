
import math

def f(x):
    return x**2 - 4

def f_prime(x):
    return 2*x 

x = 3.0 

for i in range(10): 
    fx = f(x)
    fpx = f_prime(x) # calculates derivative
    x_new = x - fx / fpx #applying Newton's formula: x_new = x - f(x)/f'(x)
    error = abs(x_new - x) #how much it changed
    
    print(f"Step {i+1}: x = {x_new:.6f}, f(x) = {fx:.6f}, error = {error:.6f}")
    
    if error < 0.0001:
        break
    
    x = x_new

print(f"\nFinal answer: {x_new:.6f}")
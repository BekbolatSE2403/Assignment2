
def f(x):
    return x**2 - 4 

a = 1  # left bound f(1) = -3
b = 3  # right bound f(3) = 5

for i in range(10):
    fa = f(a)
    fb = f(b)
    
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)
    
    print(f"Step {i+1}: x = {c:.6f}, f(x) = {fc:.6f}")
    
    if abs(fc) < 0.0001: # stop if f(c) is close enough
        break
    

    if fa * fc < 0:
        b = c  # root between a and c
    else:
        a = c  # root between c and b

print(f"\nFinal answer: {c:.6f}")
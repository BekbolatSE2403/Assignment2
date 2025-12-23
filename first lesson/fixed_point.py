import math

def g(x):
    return math.cos(x)   # we want to solve x = cos(x)
    # this is equivalent to cos(x) - x = 0

x = 0.5  # our first guess

for i in range(10):
    x_new = g(x)
    error = abs(x_new - x) 
    
    print(f"Step {i+1}: x = {x_new:.6f}, error = {error:.6f}")
    
    if error < 0.0001:
        break
    
    # update for next iteration
    x = x_new

print(f"\nFinal answer: {x_new:.6f}")
print(f"Check: cos({x_new:.6f}) = {math.cos(x_new):.6f}")
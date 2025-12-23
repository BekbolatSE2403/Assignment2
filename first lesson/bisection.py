def f(x):
    return x**2 - 4

a = 1
b = 3

for i in range(10):
    mid = (a+b)/2
    f_mid = f(mid)

    print(f"Step {i+1}: x = {mid:.4f}, f(x) = {f_mid:.4f}")

    if f(a) * f_mid < 0:
        b = mid
    else:
        a = mid
        
print(f"\nFinal answer: {mid:.4f}")
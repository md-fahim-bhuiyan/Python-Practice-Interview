def find(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c


value = find(17, 5, 11)
print(f"{value} is largest Number ")
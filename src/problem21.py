import math

def solve(a, b, c):
    d = b**2 - 4*a*c
    
    if d > 0:
        root1 = (-b - math.sqrt(d)) / (2 * a)
        root2 = (-b + math.sqrt(d)) / (2 * a)
        # Format roots: use int if the root is a whole number
        root1_str = str(int(root1)) if root1.is_integer() else str(root1)
        root2_str = str(int(root2)) if root2.is_integer() else str(root2)
        return f"{root1_str} {root2_str}"
    elif d == 0:
        root = -b / (2 * a)
        # Format root: use int if the root is a whole number
        return str(int(root)) if root.is_integer() else str(root)
    else:
        return "none"
    
a, b, c = map(float, input().split())

print(solve(a, b, c))

def root(n):
    while n >= 10:  
        n = sum(int(digit) for digit in str(n)) 
    return n

n = int(input())
result = root(n)

print(result)

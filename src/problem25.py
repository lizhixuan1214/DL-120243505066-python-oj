def sell(n):
    d = 0
    while n > 0:
        s = n // 2 + 2  
        if n <= s:
            d += 1
            break
        n -= s
        d += 1
    return d

w = int(input())

print(sell(w))

def sum(n):
    t = 0
    for i in range(1, n + 1):
        t += 1 / (3 * i - 2)
    return round(t, 5)

n = int(input())

result = sum(n)
print(result)

def calculate_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return round(total, 5)


n = int(input())
result = calculate_sum(n)
print(result)

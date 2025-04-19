def fibonacci(n):
    a = 0  # F(0)
    b = 1  # F(1)
    for i in range(2, n + 1):
        a, b = b, a + b  # 更新为 F(i-1), F(i)
    return "yes" if b % 3 == 0 else "no"

n = int(input())
print(fibonacci(n))

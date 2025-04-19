def isprime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num % 2 == 0:
        return 0
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return 0
    return 1

num = int(input())

print(isprime(num))

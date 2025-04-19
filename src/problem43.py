def is_prime(num):
    """判断一个数是否是素数"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    """找出[2, n]之间的所有素数及素数个数"""
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes, len(primes)

# 输入正整数n
n = int(input())

# 找出素数及统计个数
primes, count = find_primes(n)

# 输出结果
print(" ".join(map(str, primes)))
print(count)

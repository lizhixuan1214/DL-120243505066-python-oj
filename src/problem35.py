def zdgys(m, n):
    while n != 0:
        m, n = n, m % n
    return m

if __name__ == "__main__":
    m, n = map(int, input().split())
    result = zdgys(m, n)
    print(result)

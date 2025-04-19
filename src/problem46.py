def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_max_prime():
    """找出输入的一组正整数中的最大素数"""
    numbers = []
    while True:
        try:
            # 输入数字，以空格分隔
            user_input = input()
            numbers = list(map(int, user_input.split()))
            if numbers[-1] != 0:
                print("输入必须以0结束，请重新输入！")
                continue
            break
        except ValueError:
            print("输入包含非数字字符，请重新输入！")

    # 去掉末尾的0
    numbers = numbers[:-1]

    # 找出所有素数
    primes = [num for num in numbers if is_prime(num)]

    # 输出结果
    if primes:
        print(max(primes))
    else:
        print("no")

# 调用函数
find_max_prime()

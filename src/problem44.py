def find_perfectnumbers(n):
    perfectnumbers = []
    for num in range(1, n + 1):
        factors_sum = 1  # Start with 1 as a divisor
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors_sum += i
                if i != num // i:  # Add the pair divisor if different
                    factors_sum += num // i
        if factors_sum == num and num != 1:  # Exclude 1, check perfect number
            perfectnumbers.append(num)
    return perfectnumbers

# 输入正整数n
try:
    n = int(input())
    if n < 1:
        print("Input must be positive")
    else:
        result = find_perfectnumbers(n)
        print(" ".join(map(str, result)))
except ValueError:
    print("Invalid input")

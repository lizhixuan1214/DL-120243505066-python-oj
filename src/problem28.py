for num in range(100, 1000):
    B = num // 100
    S = (num // 10) % 10
    G = num % 10
    
    if num == B**3 + S**3 + G**3:
        print(num, end=' ')  

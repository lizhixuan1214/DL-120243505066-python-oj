for num in range(1000, 10000):
    x = num // 100  
    y = num % 100    
    
    t = x + y
    
    if t * t == num:
        print(num, end=" ")  

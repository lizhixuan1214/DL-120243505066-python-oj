def calculate_oddsum():
    
    numbers = list(map(int, input().split()))
    
    oddsum = 0
    
    for num in numbers:
        if num == 0:
            break
        if num % 2 != 0:
            oddsum += num
    
    print(oddsum)

calculate_oddsum()

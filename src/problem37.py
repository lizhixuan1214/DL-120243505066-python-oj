data = input().split()
N = int(data[0])  
numbers = list(map(int, data[1:]))  

x = 0
y = 0

for num in numbers:
    if num % 2 == 0:  
        y += num ** 3
    else:  
        x += num ** 2

print(x, y)

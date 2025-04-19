data = input().split()

numbers = []
for x in data:
    num = int(x)
    if num == 0:
        break
    numbers.append(num)

k = sum(numbers) / len(numbers) 

print(k)

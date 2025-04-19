number = input()

sum = 0

for num in number:
    x = int(num)
    if x % 2 == 0:
        sum += x

print(sum)

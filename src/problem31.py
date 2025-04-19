numbers = list(map(int, input().split()))

sum = 0
for num in numbers:
    if num < 0:
        break
    sum += num

print(sum)

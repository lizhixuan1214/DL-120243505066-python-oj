numbers = list(map(int, input().split()))

if len(numbers) != 3:
    print("错误！")
else:
    maxnumber = max(numbers)
    print(maxnumber)

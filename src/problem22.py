nums = list(map(int, input().split()))

collected = []
for num in nums:
    if num == 0:
        break  
    if num > 0:
        collected.append(num)

if collected:
    print(max(collected))
else:
    print("无解")

data = input().split()

numbers = []
for x in data:
    num = int(x)
    if num == 0:
        break  
    numbers.append(num)

count = len(numbers)
maxx = max(numbers) if numbers else 0  # 处理空列表的情况

# 输出结果
print(f"{count} {maxx}")

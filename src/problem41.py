data = input().split()
repeat = int(data[0])  # 获取循环次数
y = data[1:]        # 获取后续所有参数

results = []

for i in range(repeat):
    x = float(y[2*i])     # 每组的第一个数是x
    n = int(y[2*i + 1])   # 每组的第二个数是n
    power = x ** n             # 计算x的n次幂
    results.append(power)

# 格式化输出（整数去小数，非整数保留两位）
output = []
for res in results:
    if res == int(res):        # 检查是否为整数
        output.append(str(int(res)))
    else:
        output.append(f"{res:.2f}")

# 输出结果
print(" ".join(output))

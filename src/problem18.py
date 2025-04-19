values = input()

value = list(map(int, values.split()))

num1, num2, answer = value

if num1 + num2 == answer:
    print("right")
else:
    print("error")

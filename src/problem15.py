number = input()

if len(number) != 5 or not number.isdigit():
    print("无效")
else:
    if number == number[::-1]:
        print("YES")
    else:
        print("NO")

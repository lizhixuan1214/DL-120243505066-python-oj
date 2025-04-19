score = int(input())

if score < 0 or score > 100:
    print("illegal")
elif 90 <= score <= 100:
    print("A")
elif 60 <= score <= 89:
    print("B")
else:
    print("C")

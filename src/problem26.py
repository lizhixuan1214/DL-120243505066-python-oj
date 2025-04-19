data = input()
datalist = list(map(int, data.split()))

repeat = datalist[0]

for score in datalist[1:]:
    if score < 60:
        print("Fail")
    else:
        print("Pass")

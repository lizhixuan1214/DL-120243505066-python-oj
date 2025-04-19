prices ={
    1: 3.1,
    2: 2.5,
    3: 4.1,
    4: 10.2
}

fruitid = int(input())

price = prices.get(fruitid, 0)
print(price)

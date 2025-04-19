score = input()
data = list(map(float, score.split()))

n = int(data[0])  
scores = data[1:] 

k = sum(scores) / n

print(k)

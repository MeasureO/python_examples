n = int(input())
a = list(map(int, input().split()))
count = [0] * 201
for i in a:
    count[i + 100] += 1
b = []
for i in range(len(count)):
    b += [i - 100] * count[i] 
for i in b:
    print(i, end=' ')

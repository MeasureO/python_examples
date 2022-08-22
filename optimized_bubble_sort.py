n = int(input())
x = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
            count += 1
print(*x, f'\n{count}')

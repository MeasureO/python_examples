n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(1, n):
    f = 0
    for j in range(n - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = 1
            s += 1
    if f == 0:
        break
print(*a)
print(s)

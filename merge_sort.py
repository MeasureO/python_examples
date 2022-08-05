def merge_list(a, b):
    na = len(a)
    nb = len(b)
    c = []
    i, j = 0, 0
    while i < na and j < nb:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c

def split_and_merge(a):
    a1 = a[:len(a) // 2]
    a2 = a[len(a) // 2:]
    
    if len(a1) > 1:
        a1 = split_and_merge(a1)
    if len(a2) > 1:
        a2 = split_and_merge(a2)
    return merge_list(a1, a2)


print(*split_and_merge(list(map(int, input().split()))))
        

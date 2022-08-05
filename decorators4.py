def sort_list(func):
    def wrapper(*args, **kwargs):
        return sorted(func(*args))
    return wrapper

@sort_list
def get_list(s):
    return list(map(int, s.split()))

print(*get_list(input()))

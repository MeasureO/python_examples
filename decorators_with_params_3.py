from functools import wraps

def start_sum(start=5):
    def calc_sum(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return start + sum(func(*args))
        return wrapper
    return calc_sum

@start_sum(start=5)
def to_list(a):
    return list(map(int, a.split()))

print(to_list(input()))

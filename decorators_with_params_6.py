from functools import wraps

def func_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args))
    return wrapper

@func_dec
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))

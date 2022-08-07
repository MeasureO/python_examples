import math

# Декоратор функции с параметрами
def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper
    return func_decorator

def sin_df(x):
    return math.sin(x)

sin_df = df_decorator(dx=0.001)(sin_df)

df = sin_df(math.pi/3)

print(df)

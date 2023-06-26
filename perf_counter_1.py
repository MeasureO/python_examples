from math import factorial                   # функция из модуля math     


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def get_the_fastest_func(funcs, arg):
    import time
    a = []
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        finish_time =time.perf_counter()
        a.append((func, finish_time - start_time))
    return min(a, key=lambda x: x[1])[0]




funcs = [factorial, factorial_classic, factorial_recurrent]

print(get_the_fastest_func(funcs, 900))

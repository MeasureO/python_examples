def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable) 

def get_the_fastest_func(funcs, arg):
    import time
    a = []
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        finish_time =time.perf_counter()
        a.append((func, finish_time - start_time))
    return min(a, key=lambda x: x[1])[0]




funcs = [for_and_append, list_comprehension, list_function]

print(get_the_fastest_func(funcs, range(100_000)))

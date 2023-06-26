def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]    

def get_the_fastest_func(funcs):
    import time
    a = []
    for func in funcs:
        start_time = time.perf_counter()
        func()
        finish_time =time.perf_counter()
        a.append((func, finish_time - start_time))
    return min(a, key=lambda x: x[1])[0]




funcs = [for_and_append, list_comprehension]

print(get_the_fastest_func(funcs))

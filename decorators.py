def func_decorator(func):
    def wraper(*args, **kwargs):
        print("---  some actions ---")
        result = func(*args, **kwargs)
        print("---  some actions ---")
        return result

    return wraper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"

    

f = func_decorator(some_func)

tagged = f("python", "h1")
print(tagged)

from functools import wraps

def tag_dec(tag="h1"):
    def func_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args)}</{tag}>"   
        return wrapper
    return func_dec
    
    

@tag_dec(tag="div")
def to_low(s):
    return s.lower()

print(to_low(input()))

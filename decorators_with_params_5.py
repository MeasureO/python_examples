from functools import wraps
def chars_dec(chars=" !?"):
    def func_dec(func):
        def wrapper(*args, **kwargs):
            s = ['-' if i in " !?" else i for i in func(*args)]
            s = "".join(s)
            while "--" in s:
                s = s.replace("--", '-')
            return s
        return wrapper
    return func_dec


@chars_dec(chars="?!:;,. ")
def to_kirilitsa(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return [t[i] if i in t else i for i in s.lower()]

print(to_kirilitsa(input()))

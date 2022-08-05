def make_dict(func):
    def wrapper(*args):
        return dict(list(zip(*func(*args))))
    return wrapper
@make_dict
def get_lists(s1, s2):
    return s1.split(), s2.split()

d = get_lists(input(), input())
print(*sorted(d.items()))

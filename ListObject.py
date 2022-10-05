import sys

# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None
    def link(self, obj):
        self.next_obj = obj

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
flag = 0
for i in lst_in:
    obj = ListObject(i)
    if flag == 0:
        head_obj = obj
        flag += 1
    else:
        last_obj.link(obj)
    last_obj = obj

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for d in (dict(zip(self.FIELDS, i.split())) for i in lst_in):
            self.lst_data.append(d)
    def select(self, a, b):
        return self.lst_data[a:b + 1 if b < len(self.lst_data) - 1 else len(self.lst_data)]

#lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
db = DataBase()
db.insert(lst_in)
print(db.select(1, 2))

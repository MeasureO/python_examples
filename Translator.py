class Translator:
    d = {}
    def add(self, eng, rus):
        if eng not in self.d:
            self.d[eng] = []
        if rus not in self.d[eng]:
            self.d[eng].append(rus)
    def remove(self, eng):
        self.d.pop(eng)
    def translate(self, eng):
        return self.d.get(eng, None)


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))

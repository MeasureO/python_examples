class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Table(Goods):
    pass
class TV(Goods):
    pass
class Notebook(Goods):
    pass
class Cup(Goods):
    pass

class Cart:
    def __init__(self):
        self.goods = []
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        if indx < len(self.goods):
            del self.goods[indx]
    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]
        
        

cart = Cart()
goods = [TV("Samsung", 1000), TV("LG", 500), Table("Ikea", 100), Notebook("Lenovo", 2000), Notebook("MSI", 1500), Cup("Coffe", 50)]

for item in goods:
    cart.add(item)

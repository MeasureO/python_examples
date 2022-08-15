import random

class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Line(Figure):
        pass
    
class Rect(Figure):
        pass
    
class Ellipse(Figure):
        pass

elements = []
for i in range(217):
    a, b, c, d = [random.randint(-9, 9) for i in range(4)]
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)] ))

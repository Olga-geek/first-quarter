class Cell():
    def __init__(self,num: int):
        self.num = num

    def __add__(self, other):
        self.num = self.num + other
        return self.num

    def __sub__(self, other):
        self.num = self.num - other
        if self.num > 0:
            return self.num
        else:
            raise ValueError

    def __mul__(self, other):
        self.num = self.num * other
        return self.num

    def __truediv__(self, other):
        self.num = self.num // other
        return self.num

cell = Cell(10)
print(cell.__add__(2))
print(cell.__sub__(3))
print(cell.__mul__(3))
print(cell.__truediv__(4))
'''про make_order() не поняла'''

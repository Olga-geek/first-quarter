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
'''переделала после разбора '''
class Cell():
    def __init__(self, num):
        self.num = num

    def make_order (self, row):
        newstr = '\n'.join(["*" * row for _ in range(self.num // row)])
        return f'{newstr}\n{"*" * (self.num % row)}'

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num)
        raise ValueError("")

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(round(self.num / other.num))

cell_1 = Cell(10)
print(cell_1.make_order(3))
cell_2 = Cell(5)
print(cell_1.num + cell_2.num)
'''про make_order() все равно не поняла'''

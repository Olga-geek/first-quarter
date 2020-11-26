class Stationery:
    title = str
    def __init__(self, title):
        self.title = title

    def drow(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def drow(self):
        return f'Рисуем ручкой {self.title}'

class Pencil(Stationery):
    def drow(self):
        return f'Рисуем карандашом {self.title}'

class Handle(Stationery):
    def drow(self):
        return f'Рисуем маркером {self.title}'

stationery = Stationery('Матрешку')
pen = Pen('Матрешку')
print(pen.drow())
pencil = Pencil('Матрешку')
print(pencil.drow())
handle = Handle('Матрешку')
print(handle.drow())
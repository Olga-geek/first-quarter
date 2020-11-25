class Roud:
    _lenght = float
    _width = float
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        print(f'длина {lenght}, ширина {width}')

    def some_method_asphalt(self, weight, thick):

        return (self._lenght * self._width * weight * thick) / 1000


asphalt_thick = Roud(20, 5000)
print(f'массы асфальта : {asphalt_thick.some_method_asphalt(25, 5)} тонн')

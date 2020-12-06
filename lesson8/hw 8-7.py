class ComplexNumber():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)

    def __str__(self):
        return f'{self.a} {self.b}'
cn_1 = ComplexNumber(1, 2)
cn_2 = ComplexNumber(3, 4)
print(cn_1)
print(cn_2)
print(f'сложении чисел = {cn_1 + cn_2}')
print(f'умножение чисел = {cn_1 * cn_2}')
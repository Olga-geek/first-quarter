
from sys import argv
def my_func(a, b, c):
    return (a * b) + c

file_path, a, b, c = argv
print("выработка в часах:", a)
print("ставка в час:", b)
print("премия:", c)
print("заработной платы сотрудника:", my_func(int(a), int(b), int(c)))

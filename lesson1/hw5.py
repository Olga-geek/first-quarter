v = int(input("Введите значение Выручка:"))
z = int(input("Введите значение Издержки:"))
p = v - z
r = p / v
if v > z:
    print("Вы хорошо поработали, у вас Прибыль")
if v < z:
    print("А у вас Убыток")
if v == 0:
    print("Pribl = 0")
if (v > z or v == 0):
    print("Рентабельность", r)
worker = int(input("Введите количество рабочих:"))
if v > z:
    p = p / worker
    print("Прибыль на одного сотрудника сотрудника составила:", p)
else:
    print("Фирма отработала в ноль")
a = input("Введите несколь слов через пробел:").split()
for x, el in enumerate (a,1):
    m = el[:10]
    print(x, m)

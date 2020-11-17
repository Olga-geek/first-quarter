from math import factorial as fact

def my_f(cnt):
    x = 1
    for el in range(1, cnt + 1):
        x = fact(el)
        yield x
cnt = int(input("enter some number:"))
for y in my_f(cnt):
    print(y)



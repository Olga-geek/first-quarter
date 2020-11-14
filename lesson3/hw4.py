def my_fun(x, y):
    n = 1
    for el in range (abs(y)):
        n *= x
    return n
x = int(input("введите число:"))
y = int(input("введите число:"))

p = my_fun(x, y)
print(p)

'''''
print(pow(5, -5))
'''''
'''''
def my_fun (x,y):
    res = x ** y
    return res

a = int(input("введите число:"))
b = int(input("введите число:"))
c = my_fun(a, b)
print(c)
'''''
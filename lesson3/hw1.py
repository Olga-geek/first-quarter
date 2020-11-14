def my_n(n,m):
    if m == 0:
        return "nel'zya"
    p = n / m
    return p
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = my_n(a, b)

print(c)
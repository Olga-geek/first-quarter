l1 = [7, 5, 3, 3, 2]

n = int(input("enter the some value:"))
# l1Break = False
# for x in l1:
#     print(x)
#     if n >= x:
#         d = l1.index(x)
#         print(d,"aaaa")
#         print(l1)
#         l1.insert(d, n)
#         print(l1)
#         l1Break = True
#         break
# if not l1Break:
#     print("elseelse")
#     l1.append(n)
#     print(l1)

for x in range (0,len(l1),1):
    print(x, l1[x])
    if n >= l1[x]:
        print(x,"aaaa")
        print(l1)
        l1.insert(x, n)
        print(l1)
        break
    print(x, "pered 2if")
    print(len(l1)-1,"koko")
    if x >= len(l1)-1:
        print("elseelse")
        l1.append(n)
        print(l1)
print(l1)
    # l1.index()
    # print(l1)
# for x range n ():
#     if l1[n] == n:
#         print('yes')


    # if my_list.index(n) >= n:
    #     x = n-1
    #     m = my_list.insert(x, n)n = 1
    # print(m)

''''''
def my_fun(x, y):
    n = 1
    for el in range (abs(y)):
        n *= x
    return n
x = int(input("введите число:"))
y = int(input("введите число:"))

p = my_fun(x, y)
print(p)


# print(pow(5, -5))

# def my_fun (x,y):
#     res = x ** y
#     return res
#
# a = int(input("введите число:"))
# b = int(input("введите число:"))
# c = my_fun(a, b)
# print(c)
#

# if y >= 0:
# #     print('необходимо отрицательное число')
# # y = int(input("введите отрицательное число:"))

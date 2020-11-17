
from itertools import count

for y in count(3):
     if y > 10:
         break
     else:
         print(y)

# через yield
# def fun (cnt):
#     s = 2
#     while s < cnt:
#         s += 1
#         yield s
# d = fun(10)
# for g in d:
#     print(g)


from itertools import cycle
n = 0
for x in cycle("Dobro"):
    if n > 10:
        break
    print(x)
    n += 1


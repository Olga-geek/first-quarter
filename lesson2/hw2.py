n = input("введите любое значение через пробел:")
l1 = n.split ()
for x in range(0,len(l1)-1,2):
    l1[x],l1[x+1] = l1[x+1],l1[x]
print(l1)

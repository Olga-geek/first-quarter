l1 = [7, 5, 3, 3, 2]
n = int(input("enter the some value:"))
for x in range(0,len(l1),1):
    if n >= l1[x]:
        l1.insert(x, n)
        break
    if x >= len(l1)-1:
        l1.append(n)
print(l1)

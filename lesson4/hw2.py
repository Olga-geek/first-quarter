a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [a[x+1] for x in range(0,len(a)-1) if a[x+1]>a[x]]

print(b)

# '''''
# должно получится
# [12, 44, 4, 10, 78, 123]

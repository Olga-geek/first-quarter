from functools import reduce

def s (a, b):
    return a * b

a = [x for x in range(100, 1000+2, 2)]
print(a)
print(reduce(s, a))
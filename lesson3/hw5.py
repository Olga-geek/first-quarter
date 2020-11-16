t = 0
y = True
while y:
    a = input('Enter some number or enter X for stop:').split()
    for n in a:
        if n == 'x':
            y = False
            break
        t += int(n)
    print(t)



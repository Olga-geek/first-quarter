some_list = input('enter some number:')
with open("text5.txt", 'w+') as f_obj:
    f_obj.write(some_list)
    f_obj.tell()
    print("Текущая позиция:", f_obj.tell())
    f_obj.seek(0)
    content = f_obj.readline().split()
    total_sum = [int(el) for el in content]
    print(sum(total_sum))


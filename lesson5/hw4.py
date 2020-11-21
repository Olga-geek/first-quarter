dicter = {"One": "Один",
          "Two": "Два",
          "Three": "Три",
          "Four": "Четыре"}
print(dicter)
some_obj = open("text4.txt",'r+', encoding='utf-8')
some_wr = open('text4.txt','a', encoding='utf-8')
with  some_obj, some_wr:
    for el in some_obj:
        data = el.split('-')
        data[0] = dicter.get(data[0])
        some_wr.write(' - '.join(data))

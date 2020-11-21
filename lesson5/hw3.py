with open('text3.txt', encoding="utf8") as f_obj:
    min_cash = 20000
    n = 0
    sum_cash = 0
    for el in f_obj:
        name, cash = el.split()
        sum_cash += float(cash)
        n += 1
        if float(cash) <= min_cash:
            print(f'минимальная зарплата у {name}')
    av_cash = sum_cash / n
    print(f'средняя зарплата всех сотрудников {av_cash}')


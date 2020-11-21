import json
res =[]
dicter = {}
my_prof = 0
i = 0
with open("text7.txt", 'r', encoding='utf-8') as f_obj:
    for el in f_obj:
        name_firm, form, rev, cost = el.split()
        dicter[name_firm]= (int(rev) - int(cost))
        if dicter.get(name_firm) >= 0:
            my_prof += dicter.get(name_firm)
            i += 1
    if i != 0:
        av_prof = my_prof / i
    else:
        av_prof = 0
    res.append(dicter)
    res.append({'average_profit': av_prof})
print(res)
with open("my_json_file.json", 'w') as m_js:
    json.dump(res, m_js)
    js_str = json.dumps(res)
    print(f'Создан файл с расширением .json со следующим содержанием:\n'f'{js_str}')


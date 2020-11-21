# with open('text2.txt') as f_obj:
#     content = f_obj.read()
#     stroka = len(content.splitlines())
#     slova = len(content.split())
#     letter = len(content)
#
# print(f"total line: {stroka}")
# print(f"total words: {slova}")
# print(f"kol - vo symbol: {letter}")
#

with open('text2.txt', 'r') as f_obj:
    num = 0
    for num, line in enumerate(f_obj, 1):
        wrd = len(line.split())
        print(f'in {num} line  {wrd} words')
    print(f'total lines {num}')


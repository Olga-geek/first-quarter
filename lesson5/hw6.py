dicter = {

}
# print(dicter)
with open("text6.txt", 'r', encoding='utf-8') as f_obj:
    f_obj.seek(0)
    for el in f_obj:
        subj, line = el.split(':')
        print(subj, line)
        dicter = {subj: line}
        print(dicter)
        wrd = line.split()
        print(wrd)
print(dicter)






# dicter = {
#
# }
# print(dicter)
# with open("text6.txt", 'r', encoding='utf-8') as f_obj:
#     for line in f_obj:
#         subj, rigth = line.split(':')
#         print(f'left part: {subj}; rigth part: {rigth}')
#         wrd = rigth.split()
#         print(f'word{wrd}')
#         print('-'*24)
#         m_sum = 0
#         for word in wrd:
#             print(f'word "{word}" eparated by "(": ', end='')
#             prt = word.split()
#             print(prt)
#             for part in prt:
#                 if part.isdigit():
#                     print(f'\tpart "{part}" is digit')
#                           # m_sum += int(part)
#                 else:
#                     print(f'\tpart "{part}" is not a digit')
#         print('*'* 24)
#         res_dic = {subj: m_sum}
#         print(f'as result {res_dic}')
#
# from sys import argv
#
# script_name, first_param, second_param, third_param = argv
#
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)
# from math import sin
# print(sin(90))
#
# from sys import argv
# script_name, first_name = argv
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)


from sys import argv

def my_func (a,b,c):
    return (a * b) + c
a,b,c = argv
print(my_func(a,b,c))



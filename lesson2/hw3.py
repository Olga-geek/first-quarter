# my_dict = {1: "winter",
#            2: "winter",
#            3: "spring",
#            4: "spring",
#            5: "spring",
#            6: "summer",
#            7: "summer",
#            8: "summer",
#            9: "autumn",
#            10: "autumn",
#            11: "autumn",
#            12: "winter"
#            }
# month =int(input("введит месяц в виде целого числа от 1 до 12:"))
# n = my_dict[month]
# print(n)

my_list = ["winter","spring","summer","autmn","winter"]
month2 = int(input("введит месяц в виде целого числа от 1 до 12:"))
m = my_list[month2//3]
print(m)
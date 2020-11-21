# если будет время, посмотри пжл вот это код
# out_o = open("text.txt", "w")
# some_text = input("enter the text and press enter:")
# for x in some_text:
#     if x =='':
#         break
#     else:
#         out_o.write(some_text)
# print(file=out_o, end='\n')
# out_o.close()
out_o = open("text.txt", "a")
with out_o:
    line = input("enter the text and press enter:")
    if line == "":
        raise Exception
    else:
        out_o.writelines(f"{line}\n")



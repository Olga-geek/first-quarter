class MyException(Exception):
    def __init__(self, text):
        self.text = text

some_el = []
while True:
    try:
        element = input()
        if element.lower() == "stop":
            break
        if not element.isdigit():
            raise MyException("entered is not a number ")
        some_el.append(element)
    except MyException as err:
        print(err)
print(some_el)

class MyException(Exception):
    def __init__(self, text: str):
        self.text = text


def some_except(m, n):
    if n == 0:
        raise MyException("entered the wrong number ")
    return m/n

try:
    print(some_except(1,2))
except MyException as err:
    print(err)


class Data():
    data: str
    def __init__(self, data):
        self.data = data

    def construct(self):
        day, month, year = self.data.split('-')
        self.some_list = int(day), int(month), int(year)
        return self.some_list

    def valid(self):
        if self.some_list[2] <= 0:
            raise ValueError("invalid year entered")
        elif not (self.some_list[1] in range(1,13)):
            raise ValueError("invalid month entered")
        elif not (self.some_list[0] in range(1,32)):
            raise ValueError("invalid day entered")
        elif (self.some_list[0] == 31 and self.some_list[1] not in [1,3,5,7,8,10,12]):
            raise ValueError("invalid data entered")
        elif (self.some_list[1] == 2 and self.some_list[2] %4 !=0):
            raise ValueError("leap year invalid data")
        elif (self.some_list[0] == 30 and self.some_list[1] == 2):
            raise ValueError("invalid data for the mounth February")
        else:
            return f'the entered data {self.some_list} is correct '

dt = Data('02-02-2020')
print(dt.data)
print(dt.construct())
print(dt.valid())

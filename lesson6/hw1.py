import time
class TrafficLight:
    """атрибут приватный"""
    __color = "red"

    def running2(self, tm, color_new):
        print(f'старый свет: {self.__color}')
        self.__color = color_new
        time.sleep(tm)
        print(f'текущий свет: {self.__color}')
# '''или вот так'''
    def running(self):
        if self.__color == "red":
            print(f'свет1: {self.__color}')
            time.sleep(7)
            self.__color = "yellow"
            print(f'свет2: {self.__color}')
            time.sleep(2)
            self.__color = "green"
            print(f'свет3: {self.__color}')
            time.sleep(7)
        else:
            raise ValueError("Внимание загорелся не правильный свет")



trl = TrafficLight()
trl.running()

trl.running2(7,"yellow")
trl.running2(2,"green")
trl.running2(7,"red")









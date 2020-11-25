class Car():
    speed = float
    color = str
    name = str
    is_police = bool
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The car {self.name} to go!'

    def stop(self):
        return f'The car {self.name} to stop!'

    def turn(self, direction):
            return f'{self.color} car {self.name} to turn {direction}!'


    def shom_speed(self):
        return Car.speed


class TownCar(Car):
    def shom_speed(self):
        super().speed()
        if self.speed > 60:
            return f'The TownCar speeding {self.speed} !'
        else:
            return f'Speed of the TownCar is normal!'

class SprotCar(Car):
    pass

class WorkCar(Car):
    def shom_speed(self):
        super().speed()
        if self.speed > 40:
            return f'The WorkCar speeding {self.speed} !'
        else:
            return f'Speed of the WorkCar is normal!'

class PoliceCar(Car):
    pass

car = Car(20.5, 'white', 'Honda', False)
print( '\n'+ car.go(), car.stop(), car.turn('left'))
wc = WorkCar(50, 'white', 'Honda', False)
print( '\n' + wc.go(), wc.stop(), wc.turn('left'), wc.shom_speed())
tc = TownCar(50, 'white', 'Honda', False)
print( '\n' + tc.go(), tc.turn('right'), tc.stop(), tc.turn('around'), tc.shom_speed())






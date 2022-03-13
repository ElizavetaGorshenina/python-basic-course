class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = 80
        print(f"{self.__class__.__name__} '{self.name}' has start driving")

    def stop(self):
        self.speed = 0
        print(f"{self.__class__.__name__} '{self.name}' has stopped")

    def turn(self, direction):
        self.speed = 20
        print(f"{self.__class__.__name__} '{self.name}' has turned {direction}")

    def show_speed(self):
        print(f"Speed of {self.__class__.__name__} '{self.name}' is {self.speed} km/hr")


class TownCar(Car):

    def go(self):
        self.speed = 60
        print(f"{self.__class__.__name__} '{self.name}' has start driving")

    def show_speed(self):
        if self.speed > 60:
            print(f"Speed violation! Speed allowed for a {self.__class__.__name__} is 60 km/hr")
        else:
            print(f"Speed of {self.__class__.__name__} '{self.name}' is {self.speed} km/hr")


class SportCar(Car):

    def race(self):
        self.speed = 380
        print(f"{self.__class__.__name__} '{self.name}' is racing")


class WorkCar(Car):

    def go(self):
        self.speed = 40
        print(f"{self.__class__.__name__} '{self.name}' has start driving")

    def work(self):
        self.speed = 40
        print(f"{self.__class__.__name__} '{self.name}' is working")

    def show_speed(self):
        if self.speed > 40:
            print(f'Speed violation! Speed allowed for a {self.__class__.__name__} is 40 km/hr')
        else:
            print(f"Speed of {self.__class__.__name__} '{self.name}' is {self.speed} km/hr")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def chase(self):
        self.speed = 180
        print(f"{self.__class__.__name__} '{self.name}' is chasing")


car = Car(70, 'grey', 'Kia')
print('Car is police:', car.is_police)
print(car.speed)
town_car = TownCar(50, 'blue', 'Lincoln')
town_car.show_speed()
town_car.go()
sport_car = SportCar(150, 'red', 'Toyota GT - One Road Version')
sport_car.race()
print(sport_car.name)
work_car = WorkCar(30, 'orange', 'Komatsu')
work_car.turn('left')
work_car.stop()
print(work_car.color)
police_car = PoliceCar(65, 'white', 'BMW')
police_car.chase()
police_car.show_speed()

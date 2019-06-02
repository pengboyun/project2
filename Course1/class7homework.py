class Car():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
cars = [Car( 'car1','100km/h' ),
        Car('car2', '200km/h'),
        Car('car3', '300km/h')]
for i in cars:
    print(i.name+'速度为'+i.speed)
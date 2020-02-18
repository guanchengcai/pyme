class Animal():
    legs = ''
    animalType = ''
    place = ''
    thing = 'animal'
    def __init__(self, *args, **kwargs):
        self.legs = args[0]
        self.animalType = kwargs['animalType']
        self.place = kwargs['place']
    def run(self):
        pass

class Car():
    wheel = ''
    carType = ''
    color = ''
    thing = 'car'
    def __init__(self, whl, cartp, col):
        self.wheel = whl
        self.carType = cartp
        self.color = col
    def run(self):
        super().run()
        pass

class Tranformer(Animal,Car):
    def __init__(self, a, b, c):
        Animal.__init__(self, 4,'a', 'b', place='h', animalType='y')
    def run(self):
        super().run()

Amma = Tranformer(4, 'tiger', 'land')
van = Car(4 ,4,4)
van.run()
print(Amma.wheel)
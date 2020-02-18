
class Animal:
    clr = ""
    snd = ""
    leg = 2
    fly = True
    def __init__(self, color, sound, legs, flys):
        self.clr = color
        self.snd = sound
        self.leg = legs
        self.fly = flys

class FourLeggedAnimal(Animal):
    fly = False
    leg = 4
    def __init__(self, color, sound, amount):
        self.clr = color
        self.snd = sound

class TwoLeggedAnimal(Animal):
    fly = True
    leg = 2
    def __init__(self, color, sound, amount):
        self.clr = color
        self.snd = sound

count4LeggedAnimal = 0
class Tiger(FourLeggedAnimal):
    def __init__(self):
        pass

class Fox(FourLeggedAnimal):
    def __init__(self):
        pass

class Peacock(TwoLeggedAnimal):
    def __init__(self):
        pass

class Snake(Animal):
    def __init__(self):
        self.leg = 0
        self.fly = False

class Duck(TwoLeggedAnimal):
    def __init__(self):
        pass

zoo = []
zoo += [Tiger()] * 2
zoo += [Fox()] * 4
zoo += [Peacock()] * 3
zoo += [Snake()] * 2
zoo += [Duck()] * 8
leg4 = [x for x in zoo if x.leg == 4]
print(leg4)
flies = [x for x in zoo if x.fly]
print(len(flies))






clothwear = []
class Clothe:
    clothType = ''
    clothOrder = None
    wear = False
    futureWear = None
    None
    def __init__(self, Typ, Ordr, wore):
        self.clothType = Typ
        self.clothOrder = Ordr
        self.wear = wore

class Hat(Clothe):
    clothType = 'Hat'
    clothOrder = 5
    wear = False
    def __init__(self):
        pass

class Glasses(Clothe):
    clothType = 'Glasses'
    clothOrder = 5
    wear = False
    def __init__(self):
        pass      
class Sock(Clothe):
    clothType = 'Sock'
    clothOrder = 6
    wear = False
    def __init__(self):
        pass
        

class Sheo(Clothe):
    clothType = 'Sheo'
    wear = False
    clothOrder = 8
    def __init__(self):
        pass
class UnderCloth(Clothe):
    clothType = 'UnderCloth'
    clothOrder = 1
    wear = False
    def __init__(self):    
        pass
        

class TShirt(Clothe):
    clothType = 'TShirt'
    wear = False
    clothOrder = 2
    def __init__(self):
        pass
class Undie(Clothe):
    clothType = 'Undie'
    clothOrder = 1
    wear = False
    def __init__(self):
        pass
class Pants(Clothe):
    clothType = 'Pants'
    wear = False
    clothOrder = 2
    def __init__(self):
        pass
cloth = []
cloth.append(Sheo())
cloth.append(Hat())
cloth.append(TShirt())
cloth.append(Sock())
cloth.append(Undie())
cloth.append(Glasses())
cloth.append(UnderCloth())
cloth.append(Pants())
b = Pants()
def PutON(cloth):
    d2 = []
    for x in cloth:
        d2.append(x)
    def sortInTermsOfOrder(val):
        return val.clothOrder
    d2.sort(key=sortInTermsOfOrder)
    return d2
    

print (PutON(cloth))
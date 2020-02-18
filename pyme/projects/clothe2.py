clothe1 = 'Hat'
clothe2 = 'Glasses'
clothe3 = 'Sheo'
clothe4 = 'Sock'
clothe5 = 'Tshirt'
clothe6 = 'Pants'
clothe7 = 'Undie'
clothe8 = 'Undercloth'
arr = [clothe1, clothe2, clothe3, clothe4, clothe5, clothe6, clothe7, clothe8]
state = True
clothe = []
while state:
    temparr = ", ".join(str(z) for z in arr)
    y = input('enter clothe:' + temparr + '  :')
    if y in arr:
        clothe.append(y)
        arr.remove(y)
    else:
        print('please enter a valid value')
    if len(arr)== 0:
        state = False

def start(array):
    D={}
    for x in array:
        if x == 'Tshirt':
            D [x] = 'Undercloth'
        elif x == 'Pants':
            D [x] = ['Undie','Sheo']
        elif x == 'Sheo':
            D [x] = 'Sock'
        else:
            D [x] = None
    return dict(D)
Dictionary = {}
cloth = []
Dictionary = start(clothe)
print(Dictionary.items())
while len(Dictionary) > 0:
    for x,y in Dictionary.items():
        wearible = y
        hi = wearible in cloth
        if y == None:
            cloth.append(x)
        elif hi == False:
            continue
        else:
            cloth.append(x)
    for x in cloth:
        if x not in Dictionary:
            continue
        else:
            Dictionary.pop(x)
print(cloth)
        
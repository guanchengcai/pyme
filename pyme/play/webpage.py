import turtle
class Page:
    title = None
    item = {}
    def __init__(self, titl, itm):
        self.title = titl
        self.item = itm
        global allPages
        allPages.append(self)
        if titl == 'main':
            self.swapscreen(titl)

    def box(self,thing=''):
        for x, y in self.item.items():
            if thing == '':
                if len(y) != 8:
                    global links
                    things = links
                else:
                    things = y[7]
            a,b,c,d,d2,size,margin,e = y[0], y[1], y[2], y[3], y[4], y[5], y[6], things
            turtle.up()
            turtle.pensize(5)
            turtle.pencolor('light blue')
            turtle.goto(a+d,b+d2)
            turtle.down()
            turtle.fillcolor(c)
            turtle.begin_fill()
            turtle.goto(a-d,b+d2)
            turtle.goto(a-d,b-d2)
            turtle.goto(a+d,b-d2)
            turtle.goto(a+d,b+d2)
            turtle.end_fill()
            turtle.up()
            turtle.goto(a,b+d2+margin)
            turtle.color('black')
            turtle.write(x.title(), align="center", font=("Arial", size, "normal"))
            turtle.color('blue')
            i = 1
            place1 = -230
            place2 = -150
            for z in e:
                i += 1
                turtle.goto(place1 , place2)
                turtle.write(z.title(), align='left')
                place2 += -10
                if i == 4:
                    i = 1
                    place1 += 50
                    place2 = -150

    def swapscreen(self, ttle):
        turtle.clear()
        turtle.up()
        turtle.speed(0)
        turtle.pensize(10)
        turtle.goto(-300,200)
        turtle.pencolor('grey')
        turtle.down()
        turtle.goto(300,200)
        turtle.goto(300,-200)
        turtle.goto(-300,-200)
        turtle.goto(-300,200)
        turtle.up()
        turtle.down()
        turtle.fillcolor('light grey')
        turtle.begin_fill()
        turtle.goto(-295,190)
        turtle.goto(295,190)
        turtle.goto(295,130)
        turtle.goto(-295,130)
        turtle.goto(-295,190)
        turtle.end_fill()
        turtle.begin_fill()
        turtle.goto(-295,-190)
        turtle.goto(295,-190)
        turtle.goto(295,-130)
        turtle.goto(-295,-130)
        turtle.goto(-295,-190)
        turtle.end_fill()
        turtle.up()
        turtle.goto(-280,180)
        turtle.dot(15,'red')
        turtle.goto(-260,180)
        turtle.dot(15,'yellow')
        turtle.goto(-240,180)
        turtle.dot(15,'green')
        turtle.up()
        turtle.pensize(30)
        turtle.pencolor('white')
        turtle.goto(-280,150)
        turtle.down()
        turtle.goto(280,150)
        turtle.up()
        turtle.goto(0,135)
        turtle.pencolor('light blue')
        turtle.write(f'www.mywebsite.com/{ttle}', align="center", font=("Arial", 20, "normal"))
        self.box()

    def cmd(self, command):
        self.swapscreen(command)
        if command == 'payment':
            scr = turtle.Screen()
            name = scr.textinput('Enter a Button','name')
            mail = scr.textinput('Enter a Button','email')
            if name == 'esc':
                pass
            else:
                anw = scr.textinput(f'hi {name}(email {mail}@gmail.com) you have paid a total amount of $1,000,000,000,000,000','')
                while anw != 'okay':
                    anw = scr.textinput(f'hi {name}(email {mail}@gmail.com) you have paid a total amount of $1000','')

import random
import json
with open('D:\\Users\\guanc\\Documents\\coding\\pyme\\pyme\\play\\webs.json','r') as a:
    web = json.load(a)
allPages = []
pagenotfoundPage = Page("404",{"page not found" : [0,0,"orange",500,100,60,-100]})
webDict = web.get('allPages')
for x,y in web.items():
    if x == 'links':
        links = y
    else:
        for y1,y2 in y.items():
            tempDict = {}
            for x1 in range(len(y2)):
                if len(list(y2)) != 8:
                    list(y2).append(links)
                tempDict = y2.copy()
            addPage = Page(y1,tempDict)

def defaltValueInput(defalt,inputs):
    if inputs.isdigit():
        return int(inputs)
    else:
        return defalt

while True:
    inpt = turtle.Screen()
    comd = inpt.textinput('Enter a Button','enter any text that is blue')
    if comd == None:
        continue
    elif comd == 'add':
        addDict1 = ''
        addDict2 = ''
        addDict3 = [] 
        addDict1 = (inpt.textinput('Enter a Button','enter: name'))
        state = True
        for thingss in allPages:
            if addDict1 == thingss.title:
                state = False
        if state:
            dictionary = {}
            links.append(addDict1) 
            num = ((defaltValueInput(0,inpt.textinput('Enter a Button','how many boxes?'))))
            for x in range(int(num)):
                addDict2 = (inpt.textinput('Enter a Button','enter: box name'))
                
                addDict3.append(defaltValueInput(0,inpt.textinput('Enter a Button','enter: box init x')))
                addDict3.append(defaltValueInput(0,inpt.textinput('Enter a Button','enter: box init y')))
                addDict3.append(inpt.textinput('Enter a Button','enter: box color'))
                addDict3.append(defaltValueInput(50,inpt.textinput('Enter a Button','enter: box length')))
                addDict3.append(defaltValueInput(50,inpt.textinput('Enter a Button','enter: box width')))
                addDict3.append(defaltValueInput(10,inpt.textinput('Enter a Button','enter: text size')))
                addDict3.append(defaltValueInput(-50,inpt.textinput('Enter a Button','enter: place')))
                addDict3.append(links)
                dictionary[addDict2] = addDict3.copy()
                addDict3.clear()
                addDict2 = ''
            
            addPage = Page(addDict1,dictionary)
    elif comd == 'save':
        pageToSave = {}
        for savePage in allPages:
            pageToSave[savePage.title] = savePage.item
        print(pageToSave)
        with open('D:\\Users\\guanc\\Documents\\coding\\pyme\\pyme\\play\\webs.json','w') as files:
            files.write(json.dumps({'links': links, 'allPages': pageToSave},indent=4))
        turtle.bye()
        exit('the end, ps: i don\'t know how to stop this message from appearing')
    elif comd == 'remove':
        thingToRemove = inpt.textinput('Enter a Button','remove what?')
        counter = 0
        for x in allPages:
            if thingToRemove == x.title:
                allPages.pop(counter)
                break
            counter +=1
        if thingToRemove in links:
            counter = 0
            for x in links:
                if thingToRemove == x:
                    links.pop(counter)
                    break
                counter +=1

    elif comd.isalnum:
        notFound = True
        for currentPage in allPages:
            if currentPage.title == comd.lower():
                currentPage.cmd(comd)
                notFound = False
        if notFound:
            pagenotfoundPage.cmd('not_found_error_404')
  
turtle.done()
print('hi')
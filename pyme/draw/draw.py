from turtle import*
from random import*
def DrawGrid():
    speed(0)
    for x in range(10):
        penup()
        goto(-300,50*x-200)
        pendown()
        goto(300,50*x-200)
    for x in range(12):
        penup()
        goto(50*x-300,-300)
        pendown()
        goto(50*x-300,300)
    penup()
    goto(0,0)
    pensize(1)
    dot(10)
#DrawGrid()
speed(0)
def DrawTree(root,y,col='#964B00',col2='green'):
    penup()
    color(col)
    goto(root+25,y-100)
    pensize(50)
    color(col)
    down()
    goto(root+25,y)
    pensize(1)
    up()
    goto(root+25,y+100)
    color(col2)
    begin_fill()
    circle(-100,steps=3)
    end_fill()
    goto(root+25,y+150)
    color(col2)
    begin_fill()
    circle(-80,steps=3)
    end_fill()
    goto(root+25,y+180)
    color(col2)
    begin_fill()
    circle(-50,steps=3)
    end_fill()

turtle2 = Turtle()
turtle2.speed(0)

def DrawTree2(root,y,col='#964B00',col2='green'):
    turtle2.penup()
    turtle2.color(col)
    turtle2.goto(root+25,y-100)
    turtle2.pensize(50)
    turtle2.color(col)
    turtle2.down()
    turtle2.goto(root+25,y)
    turtle2.pensize(1)
    turtle2.up()
    turtle2.goto(root+25,y+100)
    turtle2.color(col2)
    turtle2.begin_fill()
    turtle2.circle(-100,steps=3)
    turtle2.end_fill()
    turtle2.goto(root+25,y+150)
    turtle2.color(col2)
    turtle2.begin_fill()
    turtle2.circle(-80,steps=3)
    turtle2.end_fill()
    turtle2.goto(root+25,y+180)
    turtle2.color(col2)
    turtle2.begin_fill()
    turtle2.circle(-50,steps=3)
    turtle2.end_fill()

for z in range(3):
    for x in range(5):
        y = str(hex(randint(10,255)))
        y = y.replace('0x','')
        if len(y) == 1:
            y = '0'+y
        DrawTree(-1*x*100+randint(100,200),randint(150+15*(5-2*z),250-20*z),'#964B00','#00'+y+'00')
        y = str(hex(randint(10,255)))
        y = y.replace('0x','')
        if len(y) == 1:
            y = '0'+y
        DrawTree2(-1*x*100+randint(100,200),randint(150+15*(5-z),250-19*z),'#964B00','#00'+y+'00')


turtle2.up()
turtle2.goto(-250,0)
turtle2.down()
turtle2.color('#968000')
turtle2.pensize(100)
turtle2.goto(250,0)
pensize(1)
turtle3 = Turtle()
turtle4 = Turtle()
turtle3.speed(0)
turtle4.speed(0)
ht()
turtle2.ht()
turtle3.ht()
turtle4.ht()
for x in range(25):
    color('grey')
    turtle2.color('grey')
    turtle3.color('grey')
    turtle4.color('grey')
    up()
    turtle2.up()
    turtle3.up()
    turtle4.up()
    goto(randint(-300,300),(randint(-50,50)))
    turtle2.goto(randint(-300,300),(randint(-50,50)))
    turtle3.goto(randint(-300,300),(randint(-50,50)))
    turtle4.goto(randint(-300,300),(randint(-50,50)))
    dot(size=randint(3,10))
    turtle2.dot(size=randint(3,10))
    turtle3.dot(size=randint(3,10))
    turtle4.dot(size=randint(3,10))
for z in range(2):
    for x in range(5):
        y = str(hex(randint(10,255)))
        y = y.replace('0x','')
        if len(y) == 1:
            y = '0'+y
        DrawTree(-1*x*100+randint(100,200),randint(-200+15*(5-z),0-30*z),'#964B00','#00'+y+'00')
        DrawTree2(-1*x*100+randint(100,200),randint(-200+15*(5-z),0-30*z),'#964B00','#00'+y+'00')

done()



#all the number are calculated or experienced
#though not const, donnot change any number

from turtle import *
speed(0)
delay(0)
ht()

def drop():
    pu()
    width(12)
    pencolor("black")
    fillcolor("#00c2f5")
    setpos(190.5, 110)
    seth(120)
    pd()
    begin_fill()
    fd(69.25)
    seth(240)
    fd(69.25)
    circle(40, 240)
    end_fill()

def face():
    pu()
    width(20)
    pencolor("black")
    fillcolor("#ffc93c")
    setpos(200, 0)
    seth(90)
    pd()
    begin_fill()
    circle(200)
    end_fill()

def eye(side):
    if side =="left":
        x = 110
    else:
        x = -30
    pu()
    width(15)
    pencolor("black")
    setpos(x, 0)
    seth(90)
    pd()
    circle(40, 180)

def mouse():
    pu()
    width(15)
    pencolor("black")
    fillcolor("black")
    setpos(-100, -50)
    seth(0)
    pd()
    begin_fill()
    fd(200)
    seth(264.3)
    circle(-100.50,168.6)
    end_fill()

def tongue():
    pu()
    width(1)
    pencolor("black")
    fillcolor("#ce3d37")
    setpos(34.64, -125)
    seth(120)
    pd()
    begin_fill()
    circle(40, 120)
    seth(330)
    circle(70,60)
    end_fill()

def teeth():
    pu()
    width(5)
    pencolor("black")
    fillcolor("white")
    setpos(-90, -53)
    seth(0)
    pd()
    begin_fill()
    fd(186)
    seth(260)
    circle(-100, 20)
    seth(180)
    fd(166)
    seth(120)
    circle(-100, 20)
    end_fill()

#main
face()
mouse()
teeth()
tongue()
eye("left")
eye("right")
drop()
exitonclick()
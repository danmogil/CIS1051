import turtle;
import time;
import random

dan = turtle.Turtle()
dan.speed("fast")

def olympicRings():
    colors = ["blue", "black", "red", "yellow", "green"]
    dan.pensize(10)
    dan.pencolor("#FFFFFF")
    dan.setx(-200)
    for i in range(3):
        dan.setx(dan.xcor() + 120)
        dan.pendown()
        dan.pencolor(colors[i])
        dan.circle(50)
        dan.penup()
    dan.setx(-140)
    dan.sety(-60)
    for i in range(3, 5):
        dan.setx(dan.xcor() + 120)
        dan.pendown()
        dan.pencolor(colors[i])
        dan.circle(50)
        dan.penup()
    time.sleep(3)

def clock():
    dan.shape('turtle')
    x = 30
    for i in range(12):
        dan.pencolor(random.random(), random.random(), random.random())
        dan.up()
        dan.forward(80)
        dan.down()
        dan.forward(25)
        dan.up()
        dan.forward(25)
        dan.stamp()
        dan.home()
        dan.right(x)
        x += 30
    dan.pencolor(random.random(), random.random(), random.random())
    dan.dot()
    dan.forward(5000)
    time.sleep(3)

def initials():
    dan.pensize(6)
    dan.circle(50, 180)
    dan.left(90)
    dan.forward(100)
    dan.penup()
    dan.setx(80)
    dan.pendown()
    dan.right(180)
    dan.forward(100)
    dan.right(160)
    dan.forward(80)
    dan.left(150)
    dan.forward(80)
    dan.right(160)
    dan.forward(100)

    time.sleep(3)

def shape():
    dan.pensize(6)
    n = int(input("Number of sides: "))
    if n == 0:
        while True:
            dan.forward(1)
            dan.right(1.5)
            if abs(dan.pos()) < 1:
                break
    else:
        angle = 360 / n
        for i in range(n):
            dan.forward(100)
            dan.right(angle)
    
    time.sleep(3)

def triforce():
    dan.pensize(2)
    dan.penup()
    for i in range(2):
        dan.setx(dan.xcor() + 100)
        dan.pendown()
        dan.forward(100)
        dan.left(120)
        dan.forward(100)
        dan.left(120)
        dan.forward(100)
        dan.left(120)
        dan.penup()

    dan.sety(85)
    dan.setx(150)
    dan.pendown()
    dan.forward(100)
    dan.left(120)
    dan.forward(100)
    dan.left(120)
    dan.forward(100)
    dan.left(120)
    dan.penup()

    time.sleep(3)

# init
olympicRings()
# clock()
# initials()
# shape()
# triforce()
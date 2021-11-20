import turtle
import time
#1

def printSong(start):
    for i in range(int(start), 0, -1):
        print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer")
        print("Take one down, pass it around, " + str(i - 1) + " bottles of beer on the wall")

def xTble(num):
    num = int(num)
    x = 1
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(x, end='\t')
            x += 1
        print('')

def sumPow(num):
    num = int(num)
    out = 0
    outStr = ""
    for i in range(1, num + 1):
        if i == 1:
            outStr += str(i) + "^2"
        else:
            outStr += " + " + str(i) + "^2"
        out += i ** 2
    print(outStr + " = " + str(out))

#2

def drawSquare(myTurtle, squareSize):
    for _ in range(4):
        myTurtle.lt(90)
        myTurtle.fd(squareSize)
    time.sleep(3)

def drawRow(myTurtle, length, squareSize, pause = True):
    for i in range(length):
        myTurtle.fd(squareSize)
        myTurtle.lt(90)
        myTurtle.fd(squareSize)
        if i == length - 1:
            break
        myTurtle.bk(squareSize)
        myTurtle.rt(90)
    myTurtle.lt(90)
    myTurtle.fd(squareSize * length)
    myTurtle.lt(90)
    myTurtle.fd(squareSize)
    if pause:
        time.sleep(2)

def drawGrid(myTurtle, size, squareSize, pause = False):
    for i in range(size):
        drawRow(myTurtle, size, squareSize, pause)
        if i == size - 1:
            break
        dan.fd(squareSize)
        dan.lt(90)

def drawSquareStairs(myTurtle, height, squareSize, pause = False):
    for i in range(1, height + 5):
        drawRow(myTurtle, i, squareSize, pause)
        if i == height - 1:
            break
        dan.fd(squareSize)
        dan.lt(90)
    time.sleep(2)

def drawNgon(myTurtle, numSides, sideLength, pause = True):
    angle = 360 / numSides
    for _ in range(numSides):
        myTurtle.fd(sideLength)
        myTurtle.lt(angle)
    if pause:
        time.sleep(2)

def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes, pause = False):
    for _ in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength, pause)
        myTurtle.rt((180 * numSides) / numShapes)
    time.sleep(2)

#Bonus

#3.1

def hourG():
    print("|" + "\"" * 10 + "|")
    space = 1
    for i in range(8, 0, -2):
        print(" " * space + "\\" + "\"" * i + "/")
        space += 1
    print(" " * space + "||")
    for i in range(2, 10, 2):
        space -= 1
        print(" " * space + "/" + "\"" * i + "\\")
    print("|" + "\"" * 10 + "|")

#3.2

def art(n):
    rlen = (n * 4) - 2
    x = 0
    for _ in range(n):
        print("\\ " * x + "! " * (rlen - (x * 2)) + "/ " * x) 
        x += 2

#3.3

def drawNgonSpiralColored(myTurtle, numSides, sideLength, numShapes, pause = False):
    g = .2
    for _ in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength, pause)
        myTurtle.rt((180 * numSides) / numShapes)
        myTurtle.pencolor(.2, g, .8)
        g += .02
    time.sleep(2)

#init

#1.1
# printSong(input("Start: "))

#1.2
# xTble(input("Number: "))

#1.3
# sumPow(input("Number: "))

#2
dan = turtle.Turtle()
dan.speed('slow')

#2.1.1
# drawSquare(dan, 50)

#2.1.2
# drawRow(dan, 5, 50)

#2.1.3
# drawGrid(dan, 5, 50)

#2.1.4
# drawSquareStairs(dan, 5, 50)

#2.2.1
# drawNgon(dan, 6, 50)

#2.2.2
# drawNgonSpiral(dan, 6, 100, 35)

#Bonus

#3.1
# hourG()

#3.2
# art(4)

#3.3
# drawNgonSpiralColored(dan, 6, 100, 35)
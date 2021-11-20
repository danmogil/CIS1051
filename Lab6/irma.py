import turtle

def irma_setup():
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    with open('./data/irma.csv') as f:
        f.readline()
        initSwitch = 0
        for line in f:
            lat, lon, spd = line.split(',')[2:5]
            lat, lon, spd = float(lon), float(lat), int(spd)

            temp = 0
            
            if 157 <= spd:
                t.color('red')
                t.pensize(12)
                temp = 5
            elif 130 <= spd:
                t.color('orange')
                t.pensize(10)
                temp = 4
            elif 111 <= spd:
                t.color('yellow')
                t.pensize(8)
                temp = 3
            elif 96 <= spd:
                t.color('green')
                t.pensize(6)
                temp = 2
            elif 74 <= spd:
                t.color('blue')
                t.pensize(4)
                temp = 1
            else:
                t.color('white')
                t.pensize(1)

            if initSwitch == 0:
                t.hideturtle()
                t.pu()
                t.goto([lat, lon])
                t.pd()
                t.showturtle()
                initSwitch += 1
            else:
                t.goto([lat, lon])
                if temp > 0:
                    t.write(temp)
        turtle.exitonclick()
        
 
if __name__ == "__main__":
    irma()

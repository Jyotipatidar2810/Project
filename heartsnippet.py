import turtle
turtle.bgcolor("black")
# wn=turtle.Screen()
# wn.bgpic("IMG_20190402_144044.gif")
# # turtle.bgpic("IMG_20190402_144044.gif")
turtle.pensize(10)
turtle.pencolor("darkred")
turtle.shape("classic")

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(12)
turtle.color("darkred","red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

turtle.done()
import turtle
import time
from shapes import make_roof, build_house, make_door, tree_trunk, tree_top
#from setup import setup
from instructions import instructions

writer = turtle.Turtle()
tina = turtle.Turtle()
tommy = turtle.Turtle()
tina.hideturtle()
tommy.hideturtle()


# Custom class Draw_Turtle to draw clouds

class Draw_Turtle(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.color("black")

    def draw_cloud(self):
        self.penup()
        self.right(180)
        self.pendown()
        self.circle(-15, 180)
        self.left(90)
        self.circle(-30, 180)
        self.left(90)
        self.circle(-15, 180)
        self.forward(60)
        self.end_fill()
        self.right(180)
        self.penup()


sally = Draw_Turtle(100, 100)
johnny = Draw_Turtle(-140, 120)

sally.draw_cloud()
johnny.draw_cloud()

myscreen = turtle.Screen()


# This function changes the screen color
def change_bgcolor(x=0, y=0):
    if y > 0:
        myscreen.bgcolor("light blue")
    else:
        myscreen.bgcolor("light yellow")


myscreen.onclick(change_bgcolor)
setup(myscreen)
tina.speed(10)
instructions()

# onkey functions
myscreen.onkey(make_roof, "up")

myscreen.onkey(build_house, "down")

myscreen.onkey(make_door, "D")

myscreen.onkey(tree_trunk, "right")

myscreen.onkey(tree_top, "left")

myscreen.listen()

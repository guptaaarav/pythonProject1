import turtle

tommy = turtle.Turtle()
tina = turtle.Turtle()
tommy.hideturtle()
tina.hideturtle()


# house roof
def make_roof():
    tommy.penup()
    tommy.goto(50, 0)
    tommy.color("red")
    tommy.pendown()
    tommy.begin_fill()
    tommy.forward(100)
    tommy.left(120)
    tommy.forward(100)
    tommy.left(120)
    tommy.forward(100)
    tommy.end_fill()
    tommy.penup()


# bottom house
def build_house():
    tommy.pendown()
    tommy.color("yellow")
    tommy.begin_fill()
    tommy.setheading(270)
    for i in range(4):
        tommy.forward(100)
        tommy.left(90)
    tommy.end_fill()
    tommy.penup()


# Door
def make_door():
    tommy.penup()
    tommy.goto(80, -100)
    tommy.setheading(90)
    tommy.color("blue")
    tommy.begin_fill()
    tommy.pendown()
    tommy.forward(80)
    tommy.right(90)
    tommy.forward(50)
    tommy.right(90)
    tommy.forward(80)
    tommy.right(90)
    tommy.forward(50)
    tommy.end_fill()
    tommy.penup()


# Tree trunk
def tree_trunk():
    tina.penup()
    tina.goto(-100, -100)
    tina.pendown()
    tina.color("brown")
    tina.begin_fill()
    tina.setheading(90)
    tina.forward(100)
    tina.right(90)
    tina.forward(30)
    tina.right(90)
    tina.forward(100)
    tina.right(90)
    tina.forward(30)
    tina.end_fill()
    tina.penup()


# Tree top
def tree_top():
    tina.goto(-80, 40)
    tina.pendown()
    tina.color("green")
    tina.begin_fill()
    tina.left(45)
    tina.circle(25)
    tina.penup()

    tina.goto(-80, 40)
    tina.setheading(360)
    tina.pendown()
    tina.circle(25)
    tina.penup()

    tina.goto(-100, 0)
    tina.pendown()
    tina.circle(25)
    tina.end_fill()
    tina.penup()
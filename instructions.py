import turtle
import time
writer = turtle.Turtle()
writer.hideturtle()

# Writer turtle writes all the instructions
def instructions():
  writer.penup()
  writer.goto(-40,100)
  writer.hideturtle()
  writer.right(90)
  writer.forward(30)
  writer.write("Press up key ",None,"center","16pt bold")
  writer.forward(30)
  writer.write("Press down key",None,"center","16pt bold")
  writer.forward(30)
  writer.write("Press D",None,"center","16pt bold")
  writer.forward(30)
  writer.write("Press right key",None,"center","16pt bold")
  writer.forward(30)
  writer.write("Press left key",None,"center","16pt bold")
  time.sleep(3)
  writer.clear()
  writer.hideturtle()
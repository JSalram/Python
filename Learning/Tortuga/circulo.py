import turtle
import math

wn = turtle.Screen()
wn.title("Círculo tortuga Python")
wn.bgcolor("lightgreen")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.fillcolor("green")
leonardo.color("green")
leonardo.speed(0)

side = wn.numinput("Tamaño", "Indica el tamaño del círculo")
radius = (side * 360) / (2 * math.pi)
leonardo.penup()
leonardo.sety(radius)
leonardo.pendown()

leonardo.begin_fill()
for i in range (360):
    leonardo.forward(side)
    leonardo.right(1)
leonardo.end_fill()

wn.exitonclick()
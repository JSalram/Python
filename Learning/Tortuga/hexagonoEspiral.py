import turtle

wn = turtle.Screen()
wn.title("Hexágono espiral color - Tortuga Python")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.color("blue")
leonardo.pensize(2)
leonardo.speed(0)
leonardo.left(45)

size = 1

for i in range (147):
    leonardo.forward(size)
    leonardo.left(58)
    size += 1

wn.exitonclick()
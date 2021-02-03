import turtle

wn = turtle.Screen()
wn.title("Cuadrado espiral - Tortuga Python")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.color("blue")
leonardo.speed(0)
leonardo.left(45)

size = 1

for i in range (179):
    leonardo.forward(size)
    leonardo.left(88)
    size += 2

wn.exitonclick()
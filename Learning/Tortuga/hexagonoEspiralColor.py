import turtle

wn = turtle.Screen()
wn.title("Hexágono espiral color - Tortuga Python")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.color("blue")
leonardo.pensize(2)
leonardo.speed(0)
leonardo.left(45)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for x in range(200):
    leonardo.pencolor(colors[x % 6])
    leonardo.width(x/100 + 1)
    leonardo.forward(x)
    leonardo.left(59)

wn.exitonclick()
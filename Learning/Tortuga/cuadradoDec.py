import turtle

wn = turtle.Screen()
wn.title("Cuadrado infinito - Tortuga Python")
wn.bgcolor("lightgreen")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.color("blue")
leonardo.speed(5)

size = int(wn.numinput("Tamaño", "Indica el tamaño del cuadrado"))
dec = int(wn.numinput("Decremento", "Indica la separación que quieres que tenga"))

leonardo.penup()
leonardo.sety(size / -2)
leonardo.setx(size / -2)
leonardo.pendown()

for i in range(size // dec):
    leonardo.forward(size)
    leonardo.left(90)
    size -= dec

wn.exitonclick()
import turtle

wn = turtle.Screen()
wn.title("Cuadrado tortuga Python")
wn.bgcolor("lightgreen")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.fillcolor("red")
leonardo.color("red")

side = wn.numinput("Tamaño", "Indica un tamaño en píxeles para el cuadrado")

leonardo.begin_fill()
for i in range(4):
    leonardo.forward(side)
    leonardo.left(90)
leonardo.end_fill()

leonardo.penup()
leonardo.right(90)
leonardo.forward(side/2)
leonardo.right(90)
leonardo.forward(side/2)
leonardo.write("Cuadrado", False, "left", ("arial", int(side/4), "bold italic"))

wn.exitonclick()
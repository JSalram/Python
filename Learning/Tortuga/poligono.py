import turtle

wn = turtle.Screen()
wn.title("Polígono tortuga Python")
wn.bgcolor("lightgreen")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.fillcolor("blue")
leonardo.color("blue")

side = int(wn.numinput("Tamaño", "Indica un tamaño en píxeles para el polígono"))
side_length = int(wn.numinput("Lados", "Indica el número de lados que quieres que tenga el polígono"))

leonardo.begin_fill()
for i in range(side_length):
    leonardo.forward(side)
    leonardo.right(360/side_length)
leonardo.end_fill()

leonardo.write("Polígono", False, "right", ("arial", int(side/4), "bold italic"))

wn.exitonclick()
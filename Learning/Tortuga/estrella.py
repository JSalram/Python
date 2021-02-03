import turtle

wn = turtle.Screen()
wn.title("Estrella tortuga Python")
wn.bgcolor("lightgreen")

leonardo = turtle.Turtle()
leonardo.hideturtle()
leonardo.pensize(3)
leonardo.fillcolor("#ffa41b")
leonardo.color("#ffa41b")

side = wn.numinput("Tamaño", "Indica un tamaño en píxeles para la estrella")

leonardo.begin_fill()
for i in range (5):
    leonardo.forward(side)
    leonardo.right(144)
leonardo.end_fill()

leonardo.write("Estrella", False, "right", ("arial", int(side/4), "bold italic"))

wn.exitonclick()
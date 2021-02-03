import turtle

turtle.setup(800, 600)

wn = turtle.Screen()

leonardo = turtle.Turtle()
leonardo.penup()
leonardo.back(100)
leonardo.pendown()
leonardo.forward(300)
leonardo.left(90)
leonardo.forward(200)

wn.exitonclick()
import turtle
t = turtle.Turtle()

t.fillcolor("violet")
t.begin_fill()
for i in range(4):
    t.forward(55)
    t.right(90)
t.end_fill()

turtle.done()
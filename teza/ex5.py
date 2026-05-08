import turtle
t = turtle.Turtle()
z = 80
t.speed(1220)
colors = ["red", "blue", "green", "purple", "orange"]
for i in range(60):
    t.color(colors[i % 5])
    t.forward(i * 2)
    t.right(75)
turtle.done

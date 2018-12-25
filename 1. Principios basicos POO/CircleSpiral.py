# CircleSpiral1.py - Draw a circle spiral with color changes
import turtle
t = turtle.Pen()
t.width(2)
t.pencolor("purple")
t.speed("fastest")

colors = ["red", "green", "blue", "yellow"]
turtle.bgcolor("gray")

for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(90)

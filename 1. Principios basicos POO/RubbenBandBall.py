# RubbenBandBall.py - Draw a spiral with enter number of sides
import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
t.speed("fastest")

# You can choose between 2 a 6 sides for some cool shapes!
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]

for x in range(360):
	t.pencolor(colors[x%sides])
	t.fd(x * 3/sides + x)
	t.left(360/sides + 1)
	t.width(x * sides/200)
	t.left(90)

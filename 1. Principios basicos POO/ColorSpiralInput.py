# ColorSpiralInput.py
import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown"]
t.speed("fastest")

# Ask the user for the number of sides, between 1 and 8, with default of 4.
sides = int(turtle.numinput("Number od sides", "How many sides do you want(1-8)? ", 4, 1, 8))

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
    

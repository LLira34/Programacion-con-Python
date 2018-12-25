# ColorSpiralInput.py
import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown"]
t.speed("fastest")

# Ask the user for the number of sides, between 1 and 8, with default of 4.
name = turtle.textinput("Figure", "What's name? ")
sides = int(turtle.numinput("Number of sides", "How many sides do you want(1-8)? ", 4, 1, 8))
t.write(name, font = ("bold"))
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides)
    t.width(x*sides/200)
    
t.left(45)
t.penup()
t.fd(100)
t.left(90)
t.pendown()


# Ask the user for the number of sides, between 1 and 8, with default of 4.
name = turtle.textinput("Figure", "What's name? ")
sides = int(turtle.numinput("Number of sides", "How many sides do you want(1-8)? ", 4, 1, 8))
t.write(name, font = ("bold"))
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides)
    t.width(x*sides/200)

t.left(180)
t.penup()
t.fd(100)
t.left(90)
t.pendown()


# Ask the user for the number of sides, between 1 and 8, with default of 4.
name = turtle.textinput("Figure", "What's name? ")
sides = int(turtle.numinput("Number of sides", "How many sides do you want(1-8)? ", 4, 1, 8))
t.write(name, font = ("bold"))
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides)
    t.width(x*sides/200)

t.left(180)
t.penup()
t.fd(100)
t.left(90)
t.pendown()


# Ask the user for the number of sides, between 1 and 8, with default of 4.
name = turtle.textinput("Figure", "What's name? ")
sides = int(turtle.numinput("Number of sides", "How many sides do you want(1-8)? ", 4, 1, 8))
t.write(name, font = ("bold"))
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides)
    t.width(x*sides/200)

t.left(180)
t.penup()
t.fd(100)
t.left(90)
t.pendown()

# Ask the user for the number of sides, between 1 and 8, with default of 4.
name = turtle.textinput("Figure", "What's name? ")
sides = int(turtle.numinput("Number of sides", "How many sides do you want(1-8)? ", 4, 1, 8))
t.write(name, font = ("bold"))
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides)
    t.width(x*sides/200)

t.left(180)
t.penup()
t.fd(100)
t.left(90)
t.pendown()

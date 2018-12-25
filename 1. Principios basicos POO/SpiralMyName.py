# SpiralMyName.py - print a colorful spiral of the username
import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["red", "yellow", "blue", "green"]
t.speed("fastest")

# Ask the user's name using turtle's textinput pop-up window.
your_name = turtle.textinput("Enter your name", "What's your name? ")

# Draw a spiral of the name in the screen, written 100 times.
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x+4)/4), "bold"))
    t.left(92)

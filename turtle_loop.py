import turtle
import random

# Screen erzeugen, Fläche für Grafiken
s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pensize=3)

t.color("purple")

colors = ["green", "orange", "purple"]

for i in range(100, 0, -10):
    t.begin_fill()
    t.color(random.choice(colors))
    t.circle(i)
    t.end_fill()



turtle.done()
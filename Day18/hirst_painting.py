import turtle as t
from turtle import Screen
import random

hirst_colours = [
    (255, 0, 0),      # bright red
    (0, 162, 232),    # electric blue
    (255, 242, 0),    # yellow
    (34, 177, 76),    # green
    (237, 28, 36),    # red
    (255, 127, 39),   # orange
    (163, 73, 164),   # purple
    (63, 72, 204),    # blue
    (181, 230, 29),   # lime green
    (255, 174, 201),  # pink
    (128, 128, 128),  # grey
    (0, 0, 0),        # black
    (146, 39, 143),   # magenta
    (0, 174, 239),    # cyan
    (255, 201, 14),   # amber
    (239, 65, 35),    # red-orange
    (46, 49, 146),    # dark blue
]

timmy = t.Turtle()
timmy.penup()
y_start = -150
t.colormode(255)
timmy.pensize(20)
timmy.speed("fastest")
timmy.seth(0)
for _ in range(10):
    timmy.setpos(-220, y_start)
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(hirst_colours))
        timmy.penup()
        timmy.fd(50)
    y_start += 50


screen = Screen()
screen.exitonclick()
   

import turtle as t
import random

timmy = t.Turtle()
timmy.setx(-50)
timmy.sety(100)

colours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "lime", "brown", "navy"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range (3, 22):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)

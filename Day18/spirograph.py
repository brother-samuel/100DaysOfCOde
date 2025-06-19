import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
tim.speed(0)
tim.pensize(1)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

degrees = 5 
for _ in range(72):
    tim.seth(degrees)
    tim.pencolor(random_color())
    tim.circle(100)
    degrees += 5
    

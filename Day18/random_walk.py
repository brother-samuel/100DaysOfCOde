import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "MediumSlateBlue", "DarkSeaGreen", "LightSteelBlue", "PaleVioletRed", "CadetBlue", "DarkKhaki"]
directions = [0, 90, 180, 270]
tim.speed(0)
tim.pensize(10)

for _ in range(300):
    tim.seth(random.choice(directions))
    tim.pencolor(random.choice(colours))
    tim.forward(30)


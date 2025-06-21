from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(6):
    new_timmy = Turtle(shape="turtle")
    new_timmy.color(colours[i])
    new_timmy.penup()
    new_timmy.goto(x=-225, y=-100 + i * 40)
    turtles.append(new_timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} is a winner!")
            else:
                print(f"You've lost. The {winning_colour} is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()

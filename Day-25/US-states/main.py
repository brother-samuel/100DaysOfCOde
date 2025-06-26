import turtle
import random
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.screensize(800, 600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
states = pandas.read_csv("50_states.csv")
states_list = states['state'].tolist()
# print(states_list)
quiz_on = True
guessed_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")

while quiz_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Type in the name of a state:")
    # print(answer_state)
    answer_state = answer_state.title()
    if score == 50:
        print("You have guessed all 50 states!")
        quiz_on = False
    if answer_state in states_list:
        guessed_states.append(answer_state)
        score += 1
        # print(guessed_states)
        guessed = states[states.state == answer_state]
        write_x = guessed.x.iloc[0]
        write_y = guessed.y.iloc[0]
        writer.goto(write_x, write_y)
        writer.write(answer_state, font=("Arial", 10, "bold"))
    elif answer_state is None:
        quiz_on = False
        break


screen.exitonclick()
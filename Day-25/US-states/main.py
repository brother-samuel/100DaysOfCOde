import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states['state'].tolist()
# print(states_list)

score = 0
quiz_on = True
guessed_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")

while quiz_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Type in the name of a state:")
    # print(answer_state)
    if answer_state is None:
        missed_states = list(set(states_list) - set(guessed_states))
        pandas.Series(missed_states).to_csv("missed_states.csv")
        quiz_on = False
        break
    if score == 50:
        print("You have guessed all 50 states!")
        quiz_on = False
    answer_state = answer_state.title()
    if answer_state in states_list:
        guessed_states.append(answer_state)
        score += 1
        # print(guessed_states)
        guessed = states[states.state == answer_state]
        write_x = guessed.x.iloc[0]
        write_y = guessed.y.iloc[0]
        writer.goto(write_x, write_y)
        writer.write(answer_state, font=("Arial", 10, "bold"))



screen.exitonclick()
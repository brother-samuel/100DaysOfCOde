from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10) 

def move_backward():
    tim.backward(10)    

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen() 
screen.onkey(tim.forward, "w")  
screen.onkey(tim.left, "a")
screen.onkey(tim.right, "d")    
screen.onkey(tim.backward, "s") 
screen.onkey(tim.clear, "c")
screen.exitonclick()

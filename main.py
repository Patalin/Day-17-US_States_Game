# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Write a state name:").title()

    state_data = data[data.state == answer]

    if answer == "Exit":
        missing_states = [state for state in states if (state not in guessed_states)]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)




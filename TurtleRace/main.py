import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race? Enter a color: ")
all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -100
for i in range(0,6):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x = -225, y =y)
    y += 30
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        random_distance = random.randint(0,10)
        racer.forward(random_distance)
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()
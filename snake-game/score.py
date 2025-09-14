from turtle import Turtle
FONT = ('Courier', 13, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.number = 0
        self.write(f"Score: {self.number} ", align ="center", font = FONT)


    def increase(self):
        self.number += 1
        self.clear()
        self.write(f"Score: {self.number} ", align = "center", font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align = "center", font = FONT)

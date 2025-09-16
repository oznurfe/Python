from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def increment(self):
        self.level += 1
    def update_level(self):
        self.clear()
        self.goto(-200,200)
        self.write(f"Level: {self.level}", align = "center", font=FONT)

    def end(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=FONT)

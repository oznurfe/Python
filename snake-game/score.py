from turtle import Turtle

FONT = ('Courier', 13, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.number = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.number} High Score: {self.high_score} ", align = "center", font = FONT)

    def reset(self):
        if self.number > self.high_score:
            self.high_score = self.number
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")

        self.number = 0
        self.update_score()

    def increase(self):
        self.number += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align = "center", font = FONT)
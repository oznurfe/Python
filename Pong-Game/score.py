from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_f = 0
        self.score_s = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.score_f, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.score_s, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 300)
        self.write("SCORE", align="center", font=("Courier", 40, "normal"))

    def f_point(self):
        self.score_f += 1

    def s_point(self):
        self.score_s += 1

    def end(self):
        if self.score_f == 5:
            self.goto(0,0)
            self.write(f"First player wins!",align="center", font=("Courier", 40, "normal"))
        elif self.score_s == 5:
            self.goto(0, 0)
            self.write(f"Second player wins!", align="center", font=("Courier", 40, "normal"))


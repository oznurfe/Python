from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 10
        self.dy = 10

    def move(self):
        X_POS = self.xcor() + self.dx
        Y_POS = self.ycor() + self.dy
        self.goto(X_POS,Y_POS)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

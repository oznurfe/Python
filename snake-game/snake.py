from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
    def __init__(self):
        self.snake_body = []
        self.create()

    def create(self):
        for pos in START_POSITIONS:
            self.add_body(pos)


    def add_body(self, position):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.goto(position)
        self.snake_body.append(t)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)


    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)


    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)


    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

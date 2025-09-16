from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self, spawn_prob):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.resizemode("user")
        self.cars = []
        self.spawn_prob = spawn_prob
        self.speed = STARTING_MOVE_DISTANCE
        self.turtlesize(stretch_wid = 1.2, stretch_len = 3)
        YPOSITION = random.randint(-280, 280)
        self.goto(360,YPOSITION)

    def create_car(self):
        if random.random() < self.spawn_prob:
            self.cars.append(CarManager(self.spawn_prob))


    def go(self):
        for car in self.cars:
            car.backward(self.speed)
    def new_level(self):
        self.speed += MOVE_INCREMENT
        self.create_car()



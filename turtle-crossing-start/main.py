import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()

car = CarManager(0.1)

score = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    car.create_car()
    car.go()

    if player.ycor() > 280:
        player.start()
        car.new_level()
        score.increment()
        score.update_level()

    for c in car.cars:
        if player.distance(c) < 20:
            player.start()
            score.end()
            game_is_on = False
screen.exitonclick()
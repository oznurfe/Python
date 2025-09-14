from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
snake.move()

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    #Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #Detect collision with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect collision with the body
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()












screen.exitonclick()
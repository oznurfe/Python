from turtle import Screen
from Paddle import Paddle
from ball import Ball
from score import Score
import time
import random
screen = Screen()
screen.screensize(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

tm = 0.08

f_paddle = Paddle(400)
s_paddle = Paddle(-400)

score = Score()
ball = Ball()


screen.listen()
screen.onkeypress(f_paddle.up, "Up")
screen.onkeypress(f_paddle.down, "Down")
screen.onkeypress(s_paddle.up, "w")
screen.onkeypress(s_paddle.down, "s")
game_is_on = True



while game_is_on:
    time.sleep(tm)
    screen.update()
    ball.move()

    #Detect ball collision with wall
    if ball.ycor() > 390 or  ball.ycor() < -390:
        ball.bounce_y()

    #Detect ball collision with the paddle
    if ball.distance(f_paddle) < 30 and ball.xcor() > 320 or ball.distance(s_paddle) < 30 and ball.xcor() < -320 :
        ball.bounce_x()

    #Detect first paddle misses
    if ball.xcor() > 480:
        ball.home()
        ball.bounce_x()
        score.s_point()
        score.update_score()
        tm *= 0.9


    if ball.xcor() < -480:
        ball.home()
        ball.bounce_x()
        score.f_point()
        score.update_score()
        tm *= 0.9

    if score.score_f == 5 or score.score_s == 5:
        ball.home()
        score.end()
        game_is_on = False



screen.exitonclick()
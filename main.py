from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

delay = 0.1
game_is_on = True
score.update_score()

while game_is_on:

    time.sleep(delay)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
        delay *= 0.90

    if ball.xcor() > 410:
        score.increase_score_l()
        score.update_score()
        ball.reset_ball()

    if ball.xcor() < -410:
        score.increase_score_r()
        score.update_score()
        ball.reset_ball()





screen.exitonclick()
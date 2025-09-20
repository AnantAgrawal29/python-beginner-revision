from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

lpaddle = Paddle()
rpaddle = Paddle()

lpaddle.move_left()
rpaddle.move_right()

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

ball = Ball()
score = Score()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(rpaddle) < 50 and ball.xcor() > 340) or (ball.distance(lpaddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

    if  ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    screen.update()

screen.exitonclick()
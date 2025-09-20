import turtle as t
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("My Snake Game")
my_screen.bgcolor('black')
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right,"Right")


is_game = True
while is_game:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.move()
        score.update()
        snake.extend()

    if -280>snake.head.xcor() or snake.head.xcor()>280 or -280>snake.head.ycor() or snake.head.ycor()> 280:
        # score.game_over()
        # is_game = False
        score.reset()
        snake.reset()

    for snakes in snake.turtles[1:]:
        if snakes.distance(snake.head) <=10:
            # is_game=False
            # score.game_over() 
            score.reset()
            snake.reset()


my_screen.exitonclick()
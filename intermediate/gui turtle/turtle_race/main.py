import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, 'w')
screen.onkeypress(tim.move, 'Up')

game_is_on = True
counter = 0 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if counter%6==0:
        cars.createCars()

    if tim.ycor() > 280:
        tim.reset()
        score.updateScore()
        cars.inc()
    cars.move()
    
    for car in cars.cars:
        if(tim.distance(car)<=20):
            score.game_over()
            game_is_on=False

    counter+=1
screen.exitonclick()    

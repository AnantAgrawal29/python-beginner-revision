from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.increment = 0
    
    def createCars(self):
        car = Turtle()
        car.shape("square")
        car.color(choice(COLORS))
        car.penup()
        car.shapesize(1,2)
        car.goto(randint(260,280), randint(-240, 240))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.increment*10)
        
    def inc(self):
        self.increment += 1

    

        
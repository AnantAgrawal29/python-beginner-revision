import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
my_screen = Screen()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def dashed_lines():
    # # logic for dashed line
    tim.shape('arrow')
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def shapes():
    # # different shapes from triangle to decagon
    tim.shape('arrow')
    for i in range(3,11):
        tim.pencolor(random_color())
        for _ in range(i):
            tim.forward(100)
            tim.right(360//i)

def random_walk():
    tim.width(10)
    tim.speed('fastest')
    for _ in range(200):
        tim.pencolor(random_color())
        tim.left(random.choice([0,90,180,270]))
        tim.forward(20)

def spirograph(size=10):
    for i in range(360//size):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.right(size)

my_screen.listen()
my_screen.onkey(key="space",fun=spirograph)

my_screen.exitonclick()
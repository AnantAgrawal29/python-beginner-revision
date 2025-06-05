import colorgram
import random
import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
tim.hideturtle()
my_screen = Screen()
my_screen.setup(width=450,height=450)
t.colormode(255)
tim.width(18)
tim.fillcolor('black')

colors = colorgram.extract('hirst_painting/hirst_painting.jpg',100)
rgb_colors = []

for color in colors:
       r = color.rgb.r
       g = color.rgb.g
       b = color.rgb.b
       rgb = (r,g,b)
       rgb_colors.append(rgb)

y=-(my_screen.window_width()/2.5)
tim.up()
for _  in range(10):
    tim.setpos(-(my_screen.window_height()/2.5),y)
    for _ in range(10):
        tim.dot(20,random.choice(rgb_colors))
        tim.forward(40)
    y+=40
my_screen.exitonclick()
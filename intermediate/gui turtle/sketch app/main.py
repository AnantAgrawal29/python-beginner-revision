from turtle import Screen,Turtle

tim = Turtle()
my_screen = Screen()

def move_forward():
    tim.forward(5)

def move_backward():
    tim.left(180)
    tim.forward(5)

def turn_left():
    tim.setheading(tim.heading()+10) # or tim.left(10)

def turn_right():
    tim.setheading(tim.heading()-10) # or tim.right(10)

def clear_screen():
    tim.clear()
    tim.up()
    tim.home()

tim.speed('fastest')

my_screen.listen()
my_screen.onkey(key="w",fun=move_forward)
my_screen.onkey(key="a",fun=turn_left)
my_screen.onkey(key="s",fun=move_backward)
my_screen.onkey(key="d",fun=turn_right)
my_screen.onkey(key="c",fun=clear_screen)

my_screen.exitonclick()
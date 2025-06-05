from turtle import Turtle, Screen
import random

colors = ['red','green','blue','coral','cyan','black']
turtles = []

my_screen = Screen()
my_screen.setup(width=500,height=400)
user_bet = my_screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

for i in range(6):
    t = Turtle()
    t.penup()
    t.shape('turtle')
    t.goto(x=-230,y=(-70+30*i))
    t.color(colors[i])
    turtles.append(t)

winner = 0
while winner==0:
    for i in range(6):
        turtles[i].forward(random.randint(1,20))
        if turtles[i].xcor() > 230:
            winner = turtles[i].pencolor()
            break

if user_bet.lower() == winner:
    print('You win.')
else:
    print(f'You lose. {winner.title()} wins')
from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.turtles = []
        self.reset()
    
    def create_snake(self):
        for i in range(3):
            self.add()
            self.turtles[-1].goto(x=-20*i,y=0)

    def add(self):
        t  = Turtle()
        t.penup()
        t.shape('square')
        t.color('white')
        self.turtles.append(t)
        
    def reset(self):
        for turtle in self.turtles:
            turtle.goto(600,600)
        
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        pos = self.turtles[-1].pos()
        self.add()
        self.turtles[-1].goto(pos)

    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            new_x = self.turtles[i-1].xcor()
            new_y = self.turtles[i-1].ycor()
            self.turtles[i].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
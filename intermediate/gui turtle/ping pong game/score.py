from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.score=-1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False ,align="center",font=('Arial', 20, 'normal'))
    
    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False ,align="center",font=('Arial', 20, 'normal'))
        
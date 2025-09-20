from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.score=-1
        try:
            with open("data.txt") as file:
                content = file.read()
                self.highscore = int(content) if content.strip() else 0
        except FileNotFoundError:
            self.highscore = 0
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False ,align="center",font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.highscore))
        self.score=-1
        self.update()
    
    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}\tHigh Score: {self.highscore}", move=False ,align="center",font=('Arial', 20, 'normal'))
        
from turtle import Turtle

FONT = ("Courier", 19, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.level = 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Level {self.level}:", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        t=Turtle()
        t.penup()
        t.hideturtle()
        t.goto(0,0)
        t.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


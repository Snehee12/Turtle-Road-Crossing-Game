FONT = ("Courier", 24, "normal")
from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("black")
        self.write_score()
        

    def write_score(self):
        self.write(f"Score : {self.score}",align="center",font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=FONT)

    def increment_score(self):
        self.clear()
        self.score+=1
        self.write_score()
        
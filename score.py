from turtle import Turtle

YELLOW = 1
GREEN = 3
ORANGE = 5
RED = 7

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.goto(-390, 370)
        self.write(f"Score: {self.score}", font=("Arial",15))

    def add_point_update(self, add_point):
        self.score += add_point
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write(f"Gameover! Score: {self.score}", font=("Arial",20),align="center")
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.goto((0,-300))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color("white")
        self.st()

    def move_left(self):
        n_x = self.xcor() - 40
        self.goto(n_x,self.ycor())

    def move_right(self):
        n_x = self.xcor() + 40
        self.goto(n_x,self.ycor())

    def reset_position(self):
        self.ht()
        self.goto((0,-300))
        self.st()

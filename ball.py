from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_speed = 0.05
        self.ht()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,-280)
        self.st()
        self.x_move = 10
        self.y_move = 10

    def movement(self):
        n_x = self.xcor() + self.x_move
        n_y = self.ycor() + self.y_move
        self.goto(n_x, n_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.ht()
        self.goto(0, -280)
        self.st()
        self.bounce_x()

    def speed_inc(self):
        self.ball_speed *= 0.5

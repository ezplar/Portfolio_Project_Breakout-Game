from turtle import *
from paddle import Paddle
from ball import Ball
from wall import Wall
from score import Scoreboard
import time

#Create Screen
screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("BREAKOUT")
screen.tracer(0)

#Create One Line paddle
paddle = Paddle()

#Create Ball
ball = Ball()

#Create Wall
wall = Wall()

wall.create_wall()
print(wall.wall_list_layer8)
print(wall.wall_list_layer7)

#Create Scoreboard
score = Scoreboard()


#Paddle movemment, left and right
screen.listen()
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")

#Ball movement
is_on = True
while is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.movement()

#Ball collision with wall
    if ball.ycor() > 380 or ball.ycor() < -480:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

#Ball collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() < -280:
        ball.bounce_y()
        print(ball.distance(paddle))
        print(wall.hits)
        print(ball.ball_speed)

#Ball collision with Wall per Layer from 8 to 1
    for w in wall.wall_list_layer8:
        if ball.distance(w) < 40 and ball.ycor() >= 350:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l8)
            # print(w)
            # print(wall.wall_list_layer8)

    for w in wall.wall_list_layer7:
        if ball.distance(w) < 40 and ball.ycor() >= 320:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l7)
            # print(w)
            # print(wall.wall_list_layer7)

    for w in wall.wall_list_layer6:
        if ball.distance(w) < 40 and ball.ycor() >= 290:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l6)
            # print(w)
            # print(wall.wall_list_layer6)

    for w in wall.wall_list_layer5:
        if ball.distance(w) < 40 and ball.ycor() >= 260:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l5)
            # print(w)
            # print(wall.wall_list_layer5)

    for w in wall.wall_list_layer4:
        if ball.distance(w) < 40 and ball.ycor() >= 230:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l4)
            # print(w)
            # print(wall.wall_list_layer8)

    for w in wall.wall_list_layer3:
        if ball.distance(w) < 40 and ball.ycor() >= 200:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l3)
            # print(w)
            # print(wall.wall_list_layer7)

    for w in wall.wall_list_layer2:
        if ball.distance(w) < 40 and ball.ycor() >= 170:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l2)
            # print(w)
            # print(wall.wall_list_layer6)

    for w in wall.wall_list_layer1:
        if ball.distance(w) < 40 and ball.ycor() >= 140:
            ball.bounce_y()
            # index = wall.wall_list_layer7.index(w)
            wall.break_wall(w)
            score.add_point_update(wall.score_l1)
            # print(w)
            # print(wall.wall_list_layer5)


#Ball out of bounds at Y
    if ball.ycor() < -420:
        ball.reset_position()
        paddle.reset_position()

#Ball speed increase every 4 hits, 12 hits and contact to orange and red
    if wall.hits == 4:
        ball.speed_inc()
    if wall.hits == 12:
        ball.speed_inc()
    # if wall.hits > 12:
    #     ball.speed_inc()

    if wall.wall_list_layer8 == [] and wall.wall_list_layer7 == [] and wall.wall_list_layer6 == [] and wall.wall_list_layer5 == [] and wall.wall_list_layer4 == [] and wall.wall_list_layer3 == [] and wall.wall_list_layer2 == [] and wall.wall_list_layer1 == []:
        score.gameover()














screen.exitonclick()

#For future upgrade and improvements
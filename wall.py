from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hits = 0
        self.hideturtle()
        self.penup()
        self.wall_list_layer8 = []
        self.wall_list_layer7 = []
        self.wall_list_layer6 = []
        self.wall_list_layer5 = []
        self.wall_list_layer4 = []
        self.wall_list_layer3 = []
        self.wall_list_layer2 = []
        self.wall_list_layer1 = []
    def create_wall(self):
        x_pos8 = 0
        for n in range(8):
            x_pos8 += 90
            self.wall8 = Turtle(shape="square")
            self.score_l8 = 7
            self.wall8.hideturtle()
            self.wall8.speed(0)
            self.wall8.penup()
            self.wall8.color("red")
            self.wall8.shapesize(stretch_wid=1, stretch_len=4)
            self.wall8.setposition(-400 + x_pos8,350)
            self.wall8.showturtle()
            self.wall_list_layer8.append(self.wall8)

        x_pos7 = 0
        for n in range(8):
            x_pos7 += 90
            self.wall7 = Turtle(shape="square")
            self.score_l7 = 7
            self.wall7.hideturtle()
            self.wall7.speed(0)
            self.wall7.penup()
            self.wall7.color("red")
            self.wall7.shapesize(stretch_wid=1, stretch_len=4)
            self.wall7.setposition(-400 + x_pos7,320)
            self.wall7.showturtle()
            self.wall_list_layer7.append(self.wall7)

        x_pos6 = 0
        for n in range(8):
            x_pos6 += 90
            self.wall6 = Turtle(shape="square")
            self.score_l6 = 5
            self.wall6.hideturtle()
            self.wall6.speed(0)
            self.wall6.penup()
            self.wall6.color("orange")
            self.wall6.shapesize(stretch_wid=1, stretch_len=4)
            self.wall6.setposition(-400 + x_pos6, 290)
            self.wall6.showturtle()
            self.wall_list_layer6.append(self.wall6)

        x_pos5 = 0
        for n in range(8):
            x_pos5 += 90
            self.wall5 = Turtle(shape="square")
            self.score_l5 = 5
            self.wall5.hideturtle()
            self.wall5.speed(0)
            self.wall5.penup()
            self.wall5.color("orange")
            self.wall5.shapesize(stretch_wid=1, stretch_len=4)
            self.wall5.setposition(-400 + x_pos5, 260)
            self.wall5.showturtle()
            self.wall_list_layer5.append(self.wall5)

        x_pos4 = 0
        for n in range(8):
            x_pos4 += 90
            self.wall4 = Turtle(shape="square")
            self.score_l4 = 3
            self.wall4.hideturtle()
            self.wall4.speed(0)
            self.wall4.penup()
            self.wall4.color("green")
            self.wall4.shapesize(stretch_wid=1, stretch_len=4)
            self.wall4.setposition(-400 + x_pos4, 230)
            self.wall4.showturtle()
            self.wall_list_layer4.append(self.wall4)

        x_pos3 = 0
        for n in range(8):
            x_pos3 += 90
            self.wall3 = Turtle(shape="square")
            self.score_l3 = 3
            self.wall3.hideturtle()
            self.wall3.speed(0)
            self.wall3.penup()
            self.wall3.color("green")
            self.wall3.shapesize(stretch_wid=1, stretch_len=4)
            self.wall3.setposition(-400 + x_pos3, 200)
            self.wall3.showturtle()
            self.wall_list_layer3.append(self.wall3)

        x_pos2 = 0
        for n in range(8):
            x_pos2 += 90
            self.wall2 = Turtle(shape="square")
            self.score_l2 = 1
            self.wall2.hideturtle()
            self.wall2.speed(0)
            self.wall2.penup()
            self.wall2.color("yellow")
            self.wall2.shapesize(stretch_wid=1, stretch_len=4)
            self.wall2.setposition(-400 + x_pos2, 170)
            self.wall2.showturtle()
            self.wall_list_layer2.append(self.wall2)

        x_pos1 = 0
        for n in range(8):
            x_pos1 += 90
            self.wall1 = Turtle(shape="square")
            self.score_l1 = 1
            self.wall1.hideturtle()
            self.wall1.speed(0)
            self.wall1.penup()
            self.wall1.color("yellow")
            self.wall1.shapesize(stretch_wid=1, stretch_len=4)
            self.wall1.setposition(-400 + x_pos1, 140)
            self.wall1.showturtle()
            self.wall_list_layer1.append(self.wall1)


    def break_wall(self,index):
        # self.wall_single_object = self.wall_list_layer7[index]
        # self.wall_single_object.hideturtle()
        # self.wall_list_layer7.pop(index)
        if index in self.wall_list_layer8:
            self.hits += 1
            index.ht()
            self.wall_list_layer8.remove(index)
        if index in self.wall_list_layer7:
            self.hits += 1
            index.ht()
            self.wall_list_layer7.remove(index)

        if index in self.wall_list_layer6:
            self.hits += 1
            index.ht()
            self.wall_list_layer6.remove(index)
        if index in self.wall_list_layer5:
            self.hits += 1
            index.ht()
            self.wall_list_layer5.remove(index)

        if index in self.wall_list_layer4:
            self.hits += 1
            index.ht()
            self.wall_list_layer4.remove(index)
        if index in self.wall_list_layer3:
            self.hits += 1
            index.ht()
            self.wall_list_layer3.remove(index)

        if index in self.wall_list_layer2:
            self.hits += 1
            index.ht()
            self.wall_list_layer2.remove(index)
        if index in self.wall_list_layer1:
            self.hits += 1
            index.ht()
            self.wall_list_layer1.remove(index)
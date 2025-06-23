STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        #self.color("#FFC0CB")  Pink color not in the list
        #self.color("#40E0D0")
        self.pensize(3)
        self.penup()
        self.right(-90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(20)

    def reset(self):
        self.goto(STARTING_POSITION)

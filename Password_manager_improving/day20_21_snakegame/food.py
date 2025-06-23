from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("hot pink")
        self.speed("fastest")
        # self.refresh()

    def refresh(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)

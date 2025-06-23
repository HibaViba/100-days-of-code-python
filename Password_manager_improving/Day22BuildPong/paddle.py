from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("purple")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.setposition(position)

    def up(self):
        x, y = self.position()
        self.setposition(x, y + 20)

    def down(self):
        x, y = self.position()
        self.setposition(x, y - 20)

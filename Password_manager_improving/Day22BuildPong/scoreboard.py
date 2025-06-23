from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def add_score_to_left(self):
        self.l_score += 1
        self.update()

    def add_score_to_right(self):
        self.r_score += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-90, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(90, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

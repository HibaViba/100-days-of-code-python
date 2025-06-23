from turtle import Turtle

position_list = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.list_turtle = []
        self.creat_snake()
        self.head = self.list_turtle[0]

    def creat_snake(self):
        for position in position_list:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.list_turtle.append(new_segment)

    def grow_the_snake(self):
        self.add_segment(self.list_turtle[-1].position())

    def reset_snake(self):
        for snake in self.list_turtle:
            snake.goto(800, 800)
        self.list_turtle.clear()
        self.creat_snake()
        self.head = self.list_turtle[0]

    def move(self):
        for i in range(len(self.list_turtle) - 1, 0, -1):
            new_x = self.list_turtle[i - 1].xcor()
            new_y = self.list_turtle[i - 1].ycor()
            self.list_turtle[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

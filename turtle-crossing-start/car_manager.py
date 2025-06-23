import turtle

COLORS = ["#FF69B4", "#FF1493", "#FFB6C1", "#C71585", "#DA70D6", "#EE82EE", "#E6E6FA", "#DB7093", "#D8BFD8", "#DDA0DD"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.turtle_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 6:
            car = turtle.Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            x = 300
            y = random.randint(-250, 250)
            car.penup()
            car.goto(x, y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.turtle_speed)
    def level_up(self):
        self.turtle_speed += MOVE_INCREMENT

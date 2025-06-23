import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

Time = 0.1
screen = Screen()
# screen.bgcolor("#D3D3D3")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(Time)
    screen.update()
    # for i in range(10):
    cars.create_car()
    cars.move_cars()

    if player.ycor() > 295:
        player.reset()
        cars.level_up()
        scoreboard.next_level()
    for element in cars.cars:
        if element.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

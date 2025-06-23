from turtle import Screen
from snake import Snake
from food import Food
from score_borad import ScoreBoard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("  HIBA Snake Game  ")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.grow_the_snake()
        food.refresh()
        score_board.increase_score()
    if snake.head.xcor()>288 or snake.head.xcor()< -288 or snake.head.ycor()>288 or snake.head.ycor()< -288:
        #game_is_on = False
        score_board.reset()
        snake.reset_snake()
        #snake.move()
    for segments in snake.list_turtle[1:]:
        if snake.head.distance(segments) < 10:
            #game_is_on = False
            score_board.reset()
            snake.reset_snake()
            #snake.move()



screen.exitonclick()
import turtle

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state = screen.textinput("Guess the State","what's another state's name")
#
import pandas
df = pandas.read_csv("50_states.csv")


turtle2 = turtle.Turtle()
turtle2.hideturtle()
answer_correct = 0
game_is_on = True
while game_is_on:
    for s in df.state:
        if answer_state == s:
            answer_correct += 1
            index_0_axis = df[df.state == s].index[0]
            cor_x = df[df.state == s].x[index_0_axis]
            cor_y = df[df.state == s].y[index_0_axis]
            #print(cor_x,cor_y)
            turtle2.penup()
            turtle2.goto(cor_x,cor_y)
            turtle2.write(s,align="center", font=("Courier", 8, "normal"))
    answer_state = screen.textinput(f"{answer_correct}/50 States correct ", "what's another state's name")



screen.exitonclick()
